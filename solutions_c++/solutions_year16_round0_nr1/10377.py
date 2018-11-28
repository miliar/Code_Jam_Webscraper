#include<bits/stdc++.h>
#define i64 long long
#define mx(a,b,c) max(a,max(b,c))
#define mn(a,b,c) min(a,min(b,c))
#define eef else if
#define ff(i,s,e) for(int i=(s); i<e; i++)
#define ff2(i,s,e) for(int i=(s); i>=e; i--)
#define sf scanf
#define pf printf
#define dbug(x) cout<<"x = "<<x<<endl
#define newl cout<<"\n"
#define putcase cout<<"Case "<<++cse<<":"
using namespace std;
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
    int t , sheep , start,cse=0 ;
    cin>>t;
    while(t--){
        set<int>si;
        int temp , i=1 , num;
        cin>>start;
        while(1){
            num=(start*i);
            temp=num;
           // dbug(temp);
            while(num!=0){
                int digit;
                digit=num%10;
                num/=10;
                si.insert(digit);
               // dbug(digit);
              /*  dbug(num);
                newl;*/
            }
            //dbug(start);

             if(si.size()==10){
                cout<<"Case #"<<++cse<<": "<<temp<<endl;
                break;
             }
             else if(start==0){
                cout<<"Case #"<<++cse<<": INSOMNIA\n";
                break;
             }

            //start*=i;
            i++;
        }
    }

    return 0;
}
