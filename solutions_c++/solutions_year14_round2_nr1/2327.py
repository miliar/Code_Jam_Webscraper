#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>
#include <bitset>
#include <sstream>


#define forf(a,b) for(a=0;a<b;a++)
#define forb(a,b) for(a=b;a>0;a--)
#define count(a) for (int zzz=0;zzz<a;zzz++)
#define PI 3.14159265358979
#define MILLION 1000000
#define BILLION 1000000000
#define oo 999999999

using namespace std;

int main()
{
    int T,N,ANS;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin>>T;

    for (int i=1; i<T+1;i++){
        cin>>N;
        string* list =new string[N];
        vector<int> diff;
        string shortest="";
        for (int j=0;j<N;j++){
            cin>>list[j];
        }
        int smallest=999999;
        int pl=0;
        for (int j=0;j<N;j++){
            if (list[j].length()<smallest){
                smallest=list[j].length();
                pl=j;
            }
        }

        char last=' ';
        for (int j=0;j<list[pl].length();j++){
            if (last!=list[pl][j]){
                last=list[pl][j];
                shortest+=list[pl][j];
            }
        }
        int amount=shortest.length();

        int** table=new int*[N];
        for (int j=0;j<N;j++){
            table[j]=new int[amount];
            for (int k=0;k<amount;k++){
                table[j][k]=0;
            }
        }
        //cout<<shortest<<endl;

        bool flag=true;
        int k;
        int count,place;
        for (int j=0;j<N;j++){
            count=0;
            place=0;
            k=0;
            while ( k<list[j].length() ){
            //for (int k=0;k<list[j].length();k++){
                //printf("checking %c with %c\n",list[j][k],shortest[place]);
                if (place==amount){
                    flag=false;
                    break;
                }

                if (list[j][k]==shortest[place] ){
                    //cout<<"matches"<<endl;
                    count++;
                    k++;
                }
                else{
                    if (count==0){
                        flag=false;
                        break;
                    }
                    table[j][place]=count;
                    place+=1;


                    //cout<<"does not match, moving on, putting in "<<count<<"at"<<place<<endl;
                    count=0;
                }

            }
            if (count==0){
                flag=false;
                break;
            }
            //cout<<"MOVING ON TO NEXT CHECK"<<endl;
            table[j][place]=count;
            if (flag==false){
                break;
            }
        }
        if (flag==false){
            printf("Case #%d: Fegla Won\n",i);
            continue;
        }
        //debug
    /*    for (int j=0;j<N;j++){
            for (int k=0;k<amount;k++){
                cout<<table[j][k]<<"";
            }
            cout<<endl;
        }
*/

        int ANS=0;
        int avg;
        for (int j=0;j<amount;j++){
            double suma=0;
            for (int k=0;k<N;k++){
                suma+=table[k][j];
            }
            //cout<<"sum is "<<suma<<endl;
            avg=(int) (suma/N+0.5);
            //cout<<"avg is "<<avg<<endl;
            for (int k=0;k<N;k++){
                if (avg>table[k][j]){
                    ANS=ANS+avg-table[k][j];
                }
                else{
                    ANS=ANS+table[k][j]-avg;
                }
            }
        }


        /*char last='';
        for (int j=0;j<list[0].length();j++){
            if (last!=list[0][j]){
                last=list[0][j];
                shortest+=list[0][j];
            }
        }
        bool flag=true;
*/

        printf("Case #%d: %d\n",i,ANS);

    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}
