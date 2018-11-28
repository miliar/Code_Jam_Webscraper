#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fi;
    ofstream fo;
    int T, arr1[4][4], arr2[4][4], p, q;
    
    fi.open("A-small-attempt0.in");
    fo.open("output.out");
    fi>>T;
    for(int k=0;k<T;k++){
        fo<<"Case #"<<k+1<<": ";
        int flag=0, num=0;
        fi>>p;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fi>>arr1[i][j];
                
        fi>>q;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fi>>arr2[i][j];
        
        int m, f=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(arr1[p-1][i]==arr2[q-1][j]){
                    if(flag) {
                        f=1;
                        fo<<"Bad magician!"<<endl;
                        break;
                    }
                    flag=1;
                    num=arr1[p-1][i];
                }
            }
            if(f) break;
        }
        if(f) continue;
        else if(!flag) fo<<"Volunteer cheated!"<<endl;
        else fo<<num<<endl;
    }
    
    fi.close();
    fo.close();
}
