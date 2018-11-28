#include <iostream>
#include<string>
#include<vector>
#include<cstring>
#include<sstream>
#include <fstream>

using namespace std;

string comp(const vector<int>& v1,const vector<int> &v2,int caseNum){
    cout<<"Case #"<<caseNum<<": ";
    int answer =-1,count=0;
    for(int i=0;i<4;++i)
        for(int j=0;j<4;++j){
            if(v1[i]==v2[j]){
                answer = v1[i];
                ++count;
            }
            if(count>1)break;
        }
    if(count==1){
        cout<<answer<<endl;
        return "";
    }
    if(count>1){
        cout<< "Bad magician!"<<endl;
        return "";
    }
    cout<< "Volunteer cheated!"<<endl;
    return "";
}
void compute(int caseNum){
    fstream cout;
    cout.open("output.txt",fstream::out|fstream::app);
    int firstAnswer,secondAnswer,matrix1[4][4],matrix2[4][4];
    cin>>firstAnswer;
    for(int i=0;i<4;++i)
        for(int j=0;j<4;++j){
            cin>>matrix1[i][j];
        }
    vector<int> possibilites1;
    for(int j=0;j<4;++j)
        possibilites1.push_back(matrix1[firstAnswer-1][j]);

    cin>>secondAnswer;
    for(int i=0;i<4;++i)
        for(int j=0;j<4;++j){
            cin>>matrix2[i][j];
        }
    vector<int> possibilites2;
    for(int j=0;j<4;++j)
        possibilites2.push_back(matrix2[secondAnswer-1][j]);

    comp(possibilites1,possibilites2,caseNum);
}

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;){
        compute(++i);
    };
    return 0;
}
