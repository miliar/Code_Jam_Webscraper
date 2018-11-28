#include <bits/stdc++.h>

#define vi vector<int>
#define vb vector<bool>
#define ii pair<int, int>

using namespace std;

vector<vi> graph;

void printVec(vi a);
void printVec(vector<bool> a);
void printArr(int a[], int n);
void printArr(bool a[], int n);

int main()
{
    int t,m;
    cin >> t;
    for(m=1;m<=t;m++)
    {
        int n,k,i,j;
        string s;
        cin >> s >> k;
        n = s.size();
        int count = 0;
        for(i=0;i<n-k+1;i++)
        {
            if(s[i] == '-')
            {
                count++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                }
            }
        }
        int flag = 1;
        for(;i<n;i++)
        {
            if(s[i] == '-')
            {
                flag = 0;
                break;
            }
        }
        cout << "Case #" << m << ": ";
        if(flag)
            cout << count << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
 
void printVec(vi a)
{
    vi::iterator it;
    for(it=a.begin();it!=a.end();it++)
        cout << *it << " ";
    cout << endl;
}

void printVec(vector<bool> a)
{
    vector<bool>::iterator it;
    for(it=a.begin();it!=a.end();it++)
        cout << *it << " ";
    cout << endl;
}


void printArr(int a[], int n)
{
    int i;
    for(i=1;i<n;i++)
        cout << a[i] << " ";
    cout << endl;
}

void printArr(bool a[], int n)
{
    int i;
    for(i=1;i<n;i++)
        cout << a[i] << " ";
    cout << endl;
}