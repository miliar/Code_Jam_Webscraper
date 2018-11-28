#include<iostream>
#include<cstdio>
#include<set>
#define pi pair<int,int>
using namespace std;

int main()
{
    int T,N,i;
    cin>>T;

    for(int t=1;t<=T;t++){
        cin>>N;
        int x,sum=0;
        set<pair<int,int> >s;
        for(int i=0;i<N;i++){
                cin>>x,sum+=x;
                s.insert(make_pair(x,i));
        }
        printf("Case #%d: ",t);
        while(sum>0){

            pi p1,p = *s.rbegin();
            set<pi >::iterator it = s.end();
            s.erase(--it);
            p.first--;
            if(p.first>0)
            s.insert(p);
            sum--;
            int f=0;
            if(2 * (*s.rbegin()).first>sum){
               p1 = *s.rbegin();
               set<pi >::iterator it = s.end();
                s.erase(--it);
                p1.first--;
                sum--;
                if(p1.first>0)
                s.insert(p1);
                f=1;
            }

            cout<<(char)(p.second + 'A');
            if(f)cout<<(char)(p1.second + 'A');
            cout<<' ';
        }
        cout<<endl;
    }
    return 0;
}
