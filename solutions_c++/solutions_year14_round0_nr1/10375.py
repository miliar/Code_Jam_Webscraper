// ConsoleApplication2.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <fstream>
using namespace std;



int T,a,b,total,ans;
int arra[4][4];
int arrb[4][4];
int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
    fin>>T;
    for(int i = 0 ;i < T;i++){
        total=0;
        fin>>a;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                fin>>arra[j][k];
        fin>>b;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                fin>>arrb[j][k];
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                if(arra[a-1][j]==arrb[b-1][k]){
                    total++;
		
                    ans=arra[a-1][j];
                }
        if(total==0) fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        if(total==1) fout<<"Case #"<<i+1<<": "<<ans<<endl;
        if(total>1) fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    }

    return 0;
}


