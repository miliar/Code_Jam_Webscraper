#include <iostream>
#include <stdlib.h>

using namespace std;

int a[4][4];
int b[4][4];


int main(int argc, char *argv[])
{
  int T;
  //freopen("in.txt","r",stdin);
  //freopen("out.txt","w",stdout);
  cin >> T;
  int cas = 1;
  while(T --){
    int r1,r2;
    cin >> r1; 
    r1 --;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
                cin >> a[i][j];
        }
    }
    cin >> r2;
    r2 --;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
                cin >> b[i][j];
        } 
    }
    int cnt = 0; 
    int ans = -1;
    for(int i=0;i<4;i++){
        bool f = false;
        for(int j=0;j<4;j++){
                if(b[r2][j] == a[r1][i])f = true;
        }
        if(f) {
                cnt ++;
                ans = a[r1][i];
        }
    }
    //printf("%d",cnt);
     printf("Case #%d: ",cas++);
        if(cnt == 0){
                printf("Volunteer cheated!\n");
        }
        else if(cnt > 1){
                printf("Bad magician!\n");
        }
        else {
                printf("%d\n",ans);
        }
  }
    //system("PAUSE");	
  return 0;
}
