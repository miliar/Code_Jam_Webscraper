#include<cstdio>
#include<algorithm>
#include<numeric>
#include<tuple>
using namespace std;
int tc,n,r,p,s;
char lineup[1<<12];
inline char get_loser(char x){
    switch(x){
    case 'P':
        return 'R';
    case 'R':
        return 'S';
    case 'S':
        return 'P';
    default:
        return 0;
    }
}
inline int get_clone_index(int index){
    return index-((index&-index)>>1);
}
bool test(char ch){
    lineup[0]=ch;
    for(int i=1;i<(1<<n);++i){
        if(i&1){
            lineup[i]=get_loser(lineup[i-1]);
        }
        else{
            lineup[i]=lineup[get_clone_index(i)];
        }
    }
    // p,r,s
    tuple<int,int,int> sums=accumulate(lineup,lineup+(1<<n),make_tuple(0,0,0),[](const tuple<int,int,int>& sum,const char& el){
        tuple<int,int,int> ret=sum;
        switch(el){
        case 'P':
            ++get<0>(ret);
            break;
        case 'R':
            ++get<1>(ret);
            break;
        case 'S':
            ++get<2>(ret);
            break;
        }
        return ret;
    });
    if(get<0>(sums)==p&&get<1>(sums)==r&&get<2>(sums)==s){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    scanf("%d",&tc);
    for(int ct=1;ct<=tc;++ct){
        scanf("%d%d%d%d",&n,&r,&p,&s);
        if(test('P')||test('R')||test('S')){
            for(int spow=1;spow<=n;++spow){
                for(int ist=0;ist<(1<<n);ist+=(1<<spow)){
                    if(!lexicographical_compare(lineup+ist,lineup+ist+(1<<(spow-1)),lineup+ist+(1<<(spow-1)),lineup+ist+(1<<spow))){
                        swap_ranges(lineup+ist,lineup+ist+(1<<(spow-1)),lineup+ist+(1<<(spow-1)));
                    }
                }
            }
            printf("Case #%d: ",ct);
            for(int i=0;i<(1<<n);++i){
                printf("%c",lineup[i]);
            }
            printf("\n");
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",ct);
        }
    }
}
