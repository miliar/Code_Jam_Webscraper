#include<fstream>
#include<iostream>
#include<vector>
using namespace std;

int N_matrix[4][4];
int O_matrix[4][4];


int T;
int o;
int n;
ifstream fin("in.in");
ofstream fout("out.out",ios::app);


bool find_number(const vector<int> lData,const int data){


for(int i=0;i<lData.size();i++)
 if(lData[i]==data){ 
   return true;
 }

return false;

}

int main(){


fin>>T;
for(int t=1;t<=T;t++){
vector<int> o_data;
vector<int> n_data;
int         count=0;
int         target=0; 

fin>>o;
for(int i=0;i<4;i++)
 for(int j=0;j<4;j++)
   fin>>O_matrix[i][j];

for(int i=0;i<4;i++)
  o_data.push_back(O_matrix[o-1][i]);

fin>>n;
for(int i=0;i<4;i++)
 for(int j=0;j<4;j++)
   fin>>N_matrix[i][j];

for(int i=0;i<4;i++)
  n_data.push_back(N_matrix[n-1][i]);


for(int i=0;i<4;i++)
  if(find_number(o_data,n_data[i]))
    {
      count++;
      target=n_data[i];
    }

if(count==1){
   cout<<"case #"<<t<<": "<<target<<endl;
}else if(count>1){
   cout<<"case #"<<t<<": "<<"Bad magician!"<<endl;
}else if(count==0){
   cout<<"case #"<<t<<": "<<"Volunteer cheated!"<<endl;
}else
{
   cout<<"case #"<<t<<": "<<"error"<<endl; 
}

 
}

return 0;
}
