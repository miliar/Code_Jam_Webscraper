#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>
using namespace std;

struct Block
{
    double blk;
    int type;
    int stat;
};

void merge(Block *blk, int low, int mid, int high)
{
    Block *left = new Block[mid-low+1];
    Block *right = new Block[high-mid];
    for (int i=0; i<mid-low+1; ++i)
    {
        left[i] = blk[i+low];
    }
    for (int i=0; i<high-mid; ++i)
    {
        right[i] = blk[i+mid+1];
    }
    int s = 0, t = 0;
    for (int i=low; i<=high; ++i)
        if (s == mid-low+1)
        {
            blk[i] = right[t];
            t = t+1;
        }
        else if (t == high-mid)
        {
            blk[i] = left[s];
            s = s+1;
        }
        else if (left[s].blk <= right[t].blk)
        {
            blk[i] = left[s];
            s = s+1;
        }
        else
        {
            blk[i] = right[t];
            t = t+1;
        }
}

void merge_sort(Block *blk, int low, int high)
{
    if (low < high)
    {
        int mid = (low+high)/2;
        merge_sort(blk, low, mid);
        merge_sort(blk, mid+1, high);
        merge(blk, low, mid, high);
    }
}
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t = 0;
    cin >> t;
    for (int x=1; x<=t; ++x)
    {
        int n =0;
        cin >> n;
        Block *all_blks = new Block[2*n];
        for (int i=0; i<2*n; ++i)
        {
            cin >> all_blks[i].blk;
            if (i<n) all_blks[i].type = 0;
            else all_blks[i].type = 1;
            all_blks[i].stat = 1;
        }
        merge_sort(all_blks, 0, 2*n-1);
//        for (int i=0; i<2*n; ++i) {
//           cout << all_blks[i].blk << " " << all_blks[i].type << endl;
//        }
        int y = 0, z = 0;
        int idx_nao = 0, idx_ken = 0;
        Block *blk_nao = new Block[n];
        Block *blk_ken = new Block[n];
        for (int i=0; i<2*n; ++i)
        {
            if (all_blks[i].type == 0)
            {
                blk_nao[idx_nao] = all_blks[i];
                idx_nao += 1;
            }
            if (all_blks[i].type == 1)
            {
                blk_ken[idx_ken] = all_blks[i];
                idx_ken += 1;
            }
        }
        idx_ken = idx_nao = 0;
        while (idx_ken<n && idx_nao<n)
        {
            if (blk_nao[idx_nao].blk>blk_ken[idx_ken].blk)
            {
                z += 1;
                idx_ken++;
            }
            else
            {
                idx_nao++;
                idx_ken++;
            }
        }
        int min_ken = 0, min_nao = 0;
        int max_ken = n-1, max_nao = n-1;
        int turn = 0;
        while (max_nao >= min_nao)
        {
            if (blk_nao[max_nao].blk>blk_ken[max_ken].blk)
            {
                while (blk_nao[min_nao].blk<blk_ken[min_ken].blk)
                {
                    min_nao++;
                }
                min_nao++;

                min_ken++;
                y++;
            }
            if (blk_nao[max_nao].blk<blk_ken[max_ken].blk)
            {
                min_nao++;
                max_ken--;
            }
        }
        cout << "Case #" << x << ": " << y << " " << z << endl;
    }
    return 0;
}



