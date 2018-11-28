#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;
int main() {
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    std::ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    int ka=0;
    while(ka!=t) {
        ka++;
        int n;
        cin>>n;
        string a[n];
        for(int i=0; i<n; i++)
            cin>>a[i];
        bool for_check[n][256];
        int max=0;
        memset(for_check,0,sizeof(for_check));
        int count[n];
        int prevcount[n];
        memset(count,0,sizeof(count));
        memset(prevcount,0,sizeof(prevcount));
        bool no_ans=false;
        int reached=0;
        int ans=0;
        while(reached!=n && no_ans==false){
            reached=0;
            char x=a[0][count[0]];
            int max=0,min=1000000;
            while(count[0]<a[0].length() && a[0][count[0]]==x)
                    count[0]++;
                if(count[0]-prevcount[0]>max)
                    max=count[0]-prevcount[0];
                if(count[0]-prevcount[0]<min)
                    min=count[0]-prevcount[0];
                if(count[0]==a[0].length())
                    reached++;
                prevcount[0]=count[0];
            bool ya=true;
            for(int i=1;i<n;i++){
                if(ya && a[i][count[i]]!=x){
                    no_ans=true;
                    break;
                }
                else
                    ya=false;
                while(count[i]<a[i].length() && a[i][count[i]]==x)
                    count[i]++;
                if(count[i]-prevcount[i]>max)
                    max=count[i]-prevcount[i];
                if(count[i]-prevcount[i]<min)
                    min=count[i]-prevcount[i];
                if(count[i]==a[i].length())
                    reached++;
                prevcount[i]=count[i];

            }
            //cout<<max<<" "<<min<<endl;
            ans+=(max-min);

        }
        if(no_ans)
            cout<<"Case #"<<ka<<": "<<"Fegla Won"<<endl;
        else
            cout<<"Case #"<<ka<<": "<<ans<<endl;
    }
}
