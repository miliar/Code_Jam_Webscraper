#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
double naomi[1010];
double ken[1010];
int main(){
    ios::sync_with_stdio(false);
    int t, y, z, n, flag;
    bool ifEnd;
    fstream file, file2;
    file.open("D-large.in");
    file2.open("output.txt", ios::out);

    if(file.is_open()){
        file >> t;
        for(int tt=1 ; tt<=t ; tt++){
            file >> n;
            for(int i=0 ; i<n ; i++)
                file >> naomi[i];
            for(int i=0 ; i<n ; i++)
                file >> ken[i];

            sort(naomi, naomi+n);
            sort(ken, ken+n);

            //deceitful
            flag=0;
            y=0;
            for(int i=0 ; i<n ; i++){
                if(naomi[i] > ken[flag]){
                    flag++;
                    y++;
                }
            }
            //optimally
            flag=0;
            z=0;
            ifEnd=false;
            for(int i=0 ; i<n ; i++){
                if(naomi[i]>ken[flag]){
                    ifEnd=false;
                    do{
                        flag++;
                        if(flag==n){
                            ifEnd=true;
                            break;
                        }
                    }while(naomi[i]>ken[flag]);

                    if(!ifEnd){
                        flag++;
                        if(flag==n){
                            i++;
                        }
                    }
                }
                else{
                    flag++;
                    if(flag==n)
                        i++;
                }
                if(flag==n){
                    //if(isBigger)
                        z=n-i;
                    break;
                }

            }


            file2 << "Case #" << tt << ": " << y << " " << z << endl;
        }
        file.close();
    }
    file2.close();
    return 0;
}
