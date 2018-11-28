#include <iostream>
#include <fstream>
using namespace std;

int f(string line){
    int n=0;
    for(int i=0;i<line.size();i++)n=(n*10)+(line[i]-'0');
    return n;
}

int a1,a2;int ar1[4][4],ar2[4][4];

string f1(){
   int co=-1;
   for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
        if(ar1[a1-1][i]==ar2[a2-1][j] && co==-1){co=ar1[a1-1][i];}
        else if(ar1[a1][i]==ar2[a2][j] && co!=-1)return "Bad magician!";
    }
   }
   if(co==-1)return "Volunteer cheated!";
   string rett,ret;
   while(co>0){
    rett.push_back('0'+(co%10));
    co/=10;
   }
   for(int i=rett.size()-1;i>=0;i--)ret.push_back(rett[i]);
   return ret;
}

int main(){
    ifstream myfile;
    ofstream retfile;
    retfile.open("/home/priyadarsi/googlecodejaminput/retfile.txt");
    myfile.open("/home/priyadarsi/googlecodejaminput/A-small-attempt1.in");
    int n;
    string line;
    getline (myfile,line);n=f(line);

    for(int i=0;i<n;i++){

        getline(myfile,line);a1=f(line);

        for(int j=0;j<4;j++){
            getline(myfile,line);
            int p=0;
            for(int k=0;k<line.size();k++){
                    int te=0;
                    while(k<line.size() && line[k]!=' '){
                        te=(te*10)+(line[k]-'0');
                        k++;
                    }
                    ar1[j][p]=te;
                    p++;
            }
        }

        getline(myfile,line);a2=f(line);

        for(int j=0;j<4;j++){
            getline(myfile,line);
            int p=0;
            for(int k=0;k<line.size();k++){
                    int te=0;
                    while(k<line.size() && line[k]!=' '){
                        te=(te*10)+(line[k]-'0');
                        k++;
                    }
                    ar2[j][p]=te;
                    p++;
            }
        }
        retfile << "Case #"<<i+1<<": "<<f1()<<"\n";
    }
    myfile.close();
    return 0;
}

