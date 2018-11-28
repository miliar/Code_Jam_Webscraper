#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin("A-small-attempt0.in");   ofstream cout("salida.out");
    long long int m,r,h,x,y,cont,h1,h2,cont2,cont3,u,u1,h3,h4,c1,c2,cO,cX,q=1;
    char a;
  //  vector<vector<int> >v1(4,vector<int> (4,0));
    //

    cin>>m;
    int arr1[8]={1,-1,-1,1,1,-1,0,0};
    int arr2[8]={-1,1,-1,1,0,0,1,-1};
    bool sw;
    while (m--){
        int v1[4][4];

        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                cin>>a;
                switch(a){
                    case('X'):v1[i][j]=1; break;
                    case('T'): v1[i][j]=0;break;
                    case('O'): v1[i][j]=2;break;
                    default: v1[i][j]=-1; break;
                }
              //  cout<<" "<<v1[i][j];
                }

        }
        h=0;
        sw=false;
        cont2=0;
        cont3=0;

        r=-2;
        h1=h2=u=c1=c2=cX=cO=0;
        u1=3;
        h3=v1[0][0];
        h4=v1[0][3];
         if(h3==-1){
                h3=-2;
            }
            if(h4==-1){
                h4=-2;
            }
        for (int i=0;i<4&&!sw;i++){
            cont2=cont3=0;
            h1=v1[i][0];
            h2=v1[0][i];
            if(h1==-1){
                h1=-2;
            }
            if(h2==-1){
                h2=-2;
            }
            if (h3==v1[u][u] || 0==v1[u][u]){
                c1++;
            }
            if (h4==v1[u][u1] ||0==v1[u][u1]){
                c2++;
            }
            if(c1==4){
                 r=h3;
                break;
            }
            if(c2==4){
                r=h4;
                break;
            }
            u++;
            u1--;
            for (int j=0;j<4;j++){
                    if(h1==v1[i][j]||0==v1[i][j]){
                        cont2++;
                    }
                    if(h2==v1[j][i]||0==v1[j][i]){
                        cont3++;
                    }

                    h=v1[i][j];
                    if (h==-1||h==0){
                            if(h==-1){

                                cX++;
                            }
                        continue;
                    }

                    cont=1;


                    if (cont>=4){
                        r=h;
                        sw=true;
                        break;
                    }

                }
                 if (cont2>=4){
                        r=h1;
                        sw=true;
                        break;
                    }
                    if (cont3>=4){

                        r=h2;
                        sw=true;
                        break;
                    }
        }
        cout<<"Case #"<<q<<": ";
        if(r==-2 ){
            if (cX>0){
                    cout<<"Game has not completed"<<endl;
                }else{
                    cout<<"Draw"<<endl;
                    }
        }else{
                if(r==1){
                    cout<<"X won"<<endl;

                }else{
                    cout<<"O won"<<endl;
                }
        }

q++;


    }

     return 0;
}
