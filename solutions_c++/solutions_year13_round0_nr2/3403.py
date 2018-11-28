#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<stdlib.h>
#include<sstream>
#include<math.h>
#include<stdexcept>

using namespace std;
void cut(vector< vector<int> > &height, vector< vector<int> > lawn){
int edge;
for(int i =0;i<height.size();i++){
    int highest=0;

    for(int j =0;j<height[i].size();j++){
       if(lawn[i][j]>highest){
            highest=lawn[i][j];
           // cout<<"highest : " <<highest<<endl;
        }

    }

     for(int j =0;j<height[i].size();j++){
       if(highest<height[i][j]){
                height[i][j]=highest;
             //   cout<<height[i][j];
        }

    }
   // cout<<endl;
//cout<<"rows fine" <<endl;
}
for(int i =0;i<height[0].size();i++){
     int highest=0;

    for(int j =0;j<height.size();j++){
        if(lawn[j][i]>highest){
            highest = lawn[j][i];
          //  cout<<"highest : " <<highest<<endl;
        }

    }
    for(int j =0;j<height.size();j++){
        if(highest<height[j][i]){
                height[j][i]=highest;
             //   cout<<height[j][i];
        }

    }
 //   cout<<endl;
    // cout<<"cols fine" <<endl;
}
}
bool mowable(vector< vector<int> > lawn){
int edge;
vector< vector<int> > height;
height.resize(lawn.size());
for(int i =0;i<lawn.size();i++){
    height[i].resize(lawn[i].size());
}
if(lawn[0].size()==1){return true;}
for(int i =0;i<lawn.size();i++){
     for(int j=0;j<lawn[i].size();j++){
        height[i][j]=100;
}
}
cut(height, lawn);
for(int i =0;i<lawn.size();i++){
    for(int j =0;j<lawn[i].size();j++){
       //  cout<<"==="<<lawn[i][j] << " ! = " <<height[i][j]<<endl;
        if(lawn[i][j]!=height[i][j]){
             //   cout<<"==="<<lawn[i][j] << " ! = " <<height[i][j]<<endl<<endl<<endl;
       return false;
        }
    }
}
return true;
}

int main(){
ifstream infile;
try{
    infile.open("B-large.in", ios::in);
    cout<<"file opened success!" <<endl;
    }catch(exception e){
    cout<<e.what();
    }
ofstream outfile;
try{
    outfile.open("B-large-out.in",ios::out);
    cout<<"outfile success!" <<endl;
    }catch(exception e){
    cout<<e.what();
    }

int n;
infile>>n;
vector< vector<int> > lawn;
for(int x =0;x<n;x++){
    int depth, width;
    infile>>depth>>width;
    lawn.clear();
    for(int i=0;i<depth;i++){
            vector<int> row;
            int temp;
            row.clear();
        for(int j = 0;j<width;j++){
            infile>>temp;
            row.push_back(temp);
           // cout<<temp << " ";
        }
   // cout<<endl;
    lawn.push_back(row);
   }
   if(mowable(lawn)){
        outfile<<"Case #"<<(x+1)<<": YES"<<endl;
      //  cout<<"Case #"<<(x+1)<<": YES"<<endl;
        }
    else{
       // cout<<"Case #"<<(x+1)<<": NO"<<endl;
        outfile<<"Case #"<<(x+1)<<": NO"<<endl;
    }
cout<<x<<endl;
}





infile.close();
outfile.close();
return 0;
}
