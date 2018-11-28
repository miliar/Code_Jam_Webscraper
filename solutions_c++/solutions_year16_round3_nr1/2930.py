#include <bits/stdc++.h>

using namespace std;

struct party
{
    int key;
    int num;
};

struct compare
 {
   bool operator()(party l,party r)
   {
       return l.num< r.num;
   }
 };
int main()
{
    fstream fin;
    FILE *fout;
    fin.open("input.in",ios::in);
    fout=fopen("output.out","w");
    int t,n,j;
    fin>>t;
    for(int kase=1;kase<=t;kase++)
    {
        fprintf(fout,"Case #%d: ",kase);
        int sum=0;
        fin>>n;
        priority_queue< party, vector<party> ,compare > heap;
        party current;
        for(j=0;j<n;j++)
        {
            fin>>current.num;
            sum+=current.num;
            current.key=j;
            heap.push(current);
        }
        party top1,top2,top3;
        int m,n;
        while(!heap.empty())
        {
            top1=heap.top();
            heap.pop();
            top2=heap.top();
            heap.pop();
            m=top1.num-1;
            n=top2.num-1;
            if(heap.empty())
            {
            if(m==n)
            {
                fprintf(fout,"%c%c ",'A'+top1.key,'A'+top2.key);
                top1.num--;
                top2.num--;
                if(top1.num!=0){
                heap.push(top1);
                heap.push(top2);
                }
            }
            else if(m>n)
            {
                fprintf(fout,"%c ",'A'+top1.key);
                top1.num--;
                heap.push(top1);
                heap.push(top2);
            }
            }
            else
            {
                top3=heap.top();
                heap.pop();
                if(heap.empty())
                {
                fprintf(fout,"%c ",'A'+top1.key);
                top1.num--;
                if(top1.num!=0)
                heap.push(top1);
                heap.push(top2);
                }
                else
                {
                fprintf(fout,"%c%c ",'A'+top1.key,'A'+top2.key);
                top1.num--;
                top2.num--;
                if(top1.num!=0){
                heap.push(top1);
                heap.push(top2);
                }
                }
                heap.push(top3);
            }
        }
        fprintf(fout,"\n");
    }
    return 0;
}
