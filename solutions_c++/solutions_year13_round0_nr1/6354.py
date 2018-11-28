#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char mat[5][5];

int main(int argc, const char * argv[])
{

	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        for(int i=0;i<4;i++) scanf("%s",mat[i]);
        int flag=0;      
        int xx=0,oo=0,tt=0,pp=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(mat[i][j]=='X') xx++;
                else if(mat[i][j]=='O') oo++;
                else if(mat[i][j]=='T') tt++;
                else pp++;
            }
        }
        for(int i=0;i<4;i++){
            int x=0,o=0,t=0,p=0;
            for(int j=0;j<4;j++){
                if(mat[i][j]=='X') x++;
                else if(mat[i][j]=='O') o++;
                else if(mat[i][j]=='T') t++;
                else p++;
            }
            //cout<<x<<" "<<o<<" "<<t<<endl;
            if(x+t==4) flag=1;
            if(o+t==4) flag=2;
            if(x+t+p==4 && flag==0) flag=4;
            if(o+t+p==4 && flag==0) flag=4;
            if(p==4 && flag==0) flag=4;
        }
        //cout<<flag<<endl;
        for(int i=0;i<4;i++){
            int x=0,o=0,t=0,p=0;
            for(int j=0;j<4;j++){
                if(mat[j][i]=='X') x++;
                else if(mat[j][i]=='O') o++;
                else if(mat[j][i]=='T') t++;
                else p++;
            }
            if(x+t==4) flag=1;
            if(o+t==4) flag=2;
            if(x+t+p==4 && flag==0) flag=4;
            if(o+t+p==4 && flag==0) flag=4;
            if(p==4 && flag==0) flag=4;
        }
        //cout<<flag<<endl;
        int x=0,o=0,t=0,p=0;
        for(int i=0;i<4;i++){
            if(mat[i][i]=='X') x++;
            else if(mat[i][i]=='O') o++;
            else if(mat[i][i]=='T') t++;
            else p++;
            if(x+t==4) flag=1;
            if(o+t==4) flag=2;
            if(x+t+p==4 && flag==0) flag=4;
            if(o+t+p==4 && flag==0) flag=4;
            if(p==4 && flag==0) flag=4;
        }
        //cout<<flag<<endl;
        x=0,o=0,t=0,p=0;
        for(int i=0;i<4;i++){
            if(mat[i][3-i]=='X') x++;
            else if(mat[i][3-i]=='O') o++;
            else if(mat[i][3-i]=='T') t++;
            else p++;
            if(x+t==4) flag=1;
            if(o+t==4) flag=2;
            if(x+t+p==4 && flag==0) flag=4;
            if(o+t+p==4 && flag==0) flag=4;
            if(p==4 && flag==0) flag=4;
        }
        //cout<<x<<" "<<o<<" "<<t<<endl;
        //cout<<flag<<endl;
        if(pp!=0 && flag==0) flag=4;
        if(flag==1) printf("Case #%d: X won\n",ca);
        else if(flag==2) printf("Case #%d: O won\n",ca);
        else if(flag==4) printf("Case #%d: Game has not completed\n",ca);
        else printf("Case #%d: Draw\n",ca);
    }
    
    return 0;
}

