#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;
int box[200];
priority_queue< pair<int,int> > q;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int _ = 1 ; _ <= t ; _ ++){
        int cnt = 0;
        printf ("Case #%d:",_);
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&box[i]);
            cnt += box[i];
            q.push( make_pair(box[i],i) );
        }
        while( !q.empty()){
            if ( q.size() == 2 ){
                pair<int,int> t = q.top(); q.pop();
                pair<int,int> p = q.top(); q.pop();
                if( t.first < p.first)
                    swap(t,p);
                if( p.first != t.first ) printf(" %c",'A'+p.second);
                for(int i = 0 ; i < t.first-1 ; i++)
                    printf(" %c%c",'A'+p.second, 'A'+t.second);
                printf(" %c%c\n",'A'+p.second, 'A'+t.second);
                break;
            }
            pair<int,int> t = q.top();
            q.pop();
            printf(" %c",('A'+t.second));
            if ( t.first > 1 ){
                q.push( make_pair(t.first-1, t.second ) );
            }
        }
    }
    return 0;
}
