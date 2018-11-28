#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        int N;
        cin>>N;
        int a[N];
        long long int total=0;
        for(int i=0;i<N;i++)
        {
            cin>>a[i];
            total += a[i]; //initally stores total no of people
        }
        long long int totPpl = total;    
        cout<<"Case #"<<T<<": ";
        int majority;
        int senateEvacuated = 0;
        while(senateEvacuated != totPpl)
        {
            total = 0;
            for(int i=0;i<N;i++)
            {
                total += a[i];
            }
            majority = total/2; //finding majority
            
            int greaterInd = -1,noOfEquals = 0;
            int equalLocs[2],eqInd=0;
            for(int i=0;i<N;i++)
            {
                if(a[i] > majority)
                {
                    greaterInd = i;
                }
                if(a[i] == majority)
                {
                    noOfEquals ++;
                    equalLocs[eqInd++] = i;
                }
                    
            }
            
            if(greaterInd != -1) //clear majority
            {
                a[greaterInd] -= 2;
                cout<<(char) (greaterInd + 65);
                cout<<(char) (greaterInd + 65)<<"\t";
                senateEvacuated += 2;
                continue;
            }
            else if(noOfEquals == 1)
            {
                a[ equalLocs[0] ] -= 2;
                cout<<(char) (equalLocs[0] + 65);
                cout<<(char) (equalLocs[0] + 65)<<"\t";
                senateEvacuated += 2;
            }
           else if(noOfEquals == 2)
           {
               a[equalLocs[0]] --;
               a[equalLocs[1]] --;
               cout<<(char) (equalLocs[0] + 65);
               cout<<(char) (equalLocs[1] + 65)<<"\t";
               senateEvacuated += 2;
           }
           else
           {
               a[equalLocs[0]] --;
               cout<<(char) (equalLocs[0] + 65)<<"\t";
               senateEvacuated += 1;
           }
           if(senateEvacuated == totPpl)
           {
               cout<<endl;
               break;
           }
            
        }
    }
}