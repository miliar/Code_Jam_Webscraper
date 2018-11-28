//source here
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>

using namespace std;

const string ANS[3]={"", "Bad magician!", "Volunteer cheated!"};

int main()
{
    FILE* fp=freopen("input.txt", "r", stdin);
    FILE* fp2=freopen("output.txt", "w", stdout);
    int cases, line1, line2;
    cin>>cases;
    for(int c=1; c<=cases; ++c){
        cin>>line1;
        vector<int> arrange1, arrange2;
        int temp, same_num=0;
        for(int i=0; i<16; ++i){
            cin>>temp;
            arrange1.push_back(temp);
        }
        cin>>line2;
        for(int i=0; i<16; ++i){
            cin>>temp;
            arrange2.push_back(temp);
        }
        for(int i=0; i<4; ++i){
            for(int j=(line1-1)*4; j<line1*4; ++j){
                if(arrange1[j]==arrange2[(line2-1)*4+i]){
                    same_num++;
                    temp=arrange1[j];
                }
            }
        }
        if(same_num==1)
            cout<<"Case #"<<c<<": "<<temp<<endl;
        else if(same_num==0)
            cout<<"Case #"<<c<<": "<<ANS[2]<<endl;
        else
            cout<<"Case #"<<c<<": "<<ANS[1]<<endl;
    }
    fclose(fp);
    fclose(fp2);
    return 0;
}
