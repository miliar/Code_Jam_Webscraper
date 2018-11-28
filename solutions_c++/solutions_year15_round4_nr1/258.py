#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <bits/stdc++.h>

using namespace std;
using namespace __gnu_pbds;

typedef long long LL;

typedef tree<
    int,
    null_type,
    less<int>,
    rb_tree_tag,
    tree_order_statistics_node_update>
ordered_set;
//find_by_order
//order_of_key

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );
#define ALL(v) v.begin(),v.end()

#define X first
#define Y second
#define MP make_pair

typedef pair<int,int> pint;
typedef map<int,int> mint;

void show() {cout<<'\n';}
template<typename T,typename... Args>
void show(T a, Args... args) { cout<<a<<" "; show(args...); }
template<typename T>
void show_c(T& a) { for ( auto &x:a ){ cout<<x<<" ";}cout<<endl;  }

#define SIZE 110

char board[SIZE][SIZE];

int n,m;
bool get_up(int x,int y){
    if ( x<0 ){
        return false;
    }
    if ( board[x][y] != '.' )return true;
    else return get_up( x-1,y );
}

bool get_down(int x,int y){
    if ( x==n ){
        return false;
    }
    if ( board[x][y] != '.' )return true;
    else return get_down( x+1,y );
}
bool get_left(int x,int y){
    if ( y<0 ){
        return false;
    }
    if ( board[x][y] != '.' )return true;
    else return get_left( x,y-1 );
}
bool get_right(int x,int y){
    if ( y==m ){
        return false;
    }
    if ( board[x][y] != '.' )return true;
    else return get_right( x,y+1 );
}


int main(){

    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);

    int kase;
    scanf("%d",&kase);
    for (int kk=1;kase--;++kk){
        scanf("%d %d",&n,&m);
        for (int i=0;i<n;++i){
            scanf("%s",board[i]);
            //show( board[i] );
        }
        bool pos=true;
        int ans = 0;
        for (int i=0;i<n;++i){
            for (int j=0;j<m;++j){
                if ( board[i][j] ==  '^' ){
                    if ( !get_up( i-1,j ) ){
                        if ( get_left(i,j-1) ){

                        }else if ( get_right(i,j+1) ){

                        }else if ( get_up(i-1,j) ){

                        }else if ( get_down(i+1,j) ){

                        }else{
                            pos=false;
                        }
                        ans++;
                    }
                }else if ( board[i][j] ==  '<' ){
                    if ( !get_left( i,j-1 ) ){
                        if ( get_left(i,j-1) ){

                        }else if ( get_right(i,j+1) ){

                        }else if ( get_up(i-1,j) ){

                        }else if ( get_down(i+1,j) ){

                        }else{
                            pos=false;
                        }
                        ans++;
                    }
                }else if ( board[i][j] ==  '>' ){
                    if ( !get_right( i,j+1 ) ){
                        if ( get_left(i,j-1) ){

                        }else if ( get_right(i,j+1) ){

                        }else if ( get_up(i-1,j) ){

                        }else if ( get_down(i+1,j) ){

                        }else{
                            pos=false;
                        }
                        ans++;
                    }
                }else if ( board[i][j] ==  'v' ){
                    if ( !get_down( i+1,j ) ){
                        if ( get_left(i,j-1) ){

                        }else if ( get_right(i,j+1) ){

                        }else if ( get_up(i-1,j) ){

                        }else if ( get_down(i+1,j) ){

                        }else{
                            pos=false;
                        }
                        ans++;
                    }
                }
                if ( !pos )i=j=n+m+10;
            }
        }

        printf("Case #%d: ",kk);
        if ( !pos )printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);

    }

    return 0;
}
