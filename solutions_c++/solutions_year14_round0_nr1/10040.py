#include<iostream>
#include<fstream>
using namespace std;

int main(){
    int t, a, b, p[4][4], q[4][4], flag, num, z;
    cin>>t;
    z = t;
    ofstream fp;
    fp.open("output.txt");
    while(t--){
            cin>>a;
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++)
                    cin>>p[i][j];
            cin>>b;
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++)
                    cin>>q[i][j];
            flag = 0;
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++)
                    if(p[a-1][i] == q[b-1][j]){
                        flag++;
                        num = p[a-1][i];
                    }

            if(flag == 1)
                fp<<"Case #"<<z-t<<": "<<num<<endl;
            else if(flag > 1)
                fp<<"Case #"<<z-t<<": Bad magician!"<<endl;
            else
                fp<<"Case #"<<z-t<<": Volunteer cheated!"<<endl;
    }
    fp.close();
    return 0;
}
