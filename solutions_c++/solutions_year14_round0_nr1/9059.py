#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int a,b[2];
    int c[2][16];


    freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);


    cin>>a;
    for(int i=0;i<a;i++){

      int no=0,x;
      for(int y=0;y<2;y++){
      cin>>b[y];
      for(int j=0;j<16;j++)
            cin>>c[y][j];
      }

            for(int k=0;k<4;k++)
            {
                for(int l=0;l<4;l++)
                {
                    if(c[0][((b[0]-1)*4)+k]==c[1][((b[1]-1)*4)+l])
                        {
                            no++;
                        x=c[0][((b[0]-1)*4)+k];
                        }
                }
            }
            switch(no){
            case 4:
                case 3:
                    case 2:
                    cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
                    break;
                case 1:
                    cout<<"Case #"<<i+1<<": "<<x<<endl;
                    break;
                case 0:
                    cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
                    break;

            }


    }
    return 0;
}
