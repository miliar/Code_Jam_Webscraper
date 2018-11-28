#include<iostream>
#include<string>
#include<math.h>
#include<fstream>
#include<sstream>
#include<cstdlib>

using namespace std;
int main(int argc , char ** argv){

fstream infile(argv[1]);
   
int T;
string line;
getline(infile,line);

T=atoi(line.c_str());
for(int i=0;i<T;++i){
    getline(infile,line);
    string output;
    output.insert(0,1,*line.begin());
    char start = *line.begin();
     
    for(string::iterator it=line.begin()+1;it!=line.end();++it){
        if( *it >= start ){
            output.insert(0,1,*it);      
            start= *it;
        } else{
            output.insert(output.end(),1,*it);
        } 
         
    }

    cout<<"Case #"<<i+1<<": "<<output;
    if(i<T-1)
        cout<<endl;
}

}
