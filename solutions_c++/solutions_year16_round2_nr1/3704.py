#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<fstream>
#include<algorithm>
using namespace std;

void get_num(string str,int i,vector<int> &output, int * arr);

int main(int argc,char** argv){

    fstream infile(argv[1]);


    string line;


    int T;
    getline(infile,line);
    T=atoi(line.c_str());

    for(int t = 0 ; t<T;++t){
        getline(infile,line);

        int arr[26];
        for(int j = 0 ;j<26 ; ++j){
            arr[j]=0;
        }
        for (string::iterator it = line.begin();it<line.end();++it){
            ++arr[(*it - 65) ];     
        }

        vector<int> output;
        if(arr['W'-65] > 0 )
            get_num("TWO",2,output,arr);

        if(arr['U' - 65]> 0)
            get_num("FOUR",4,output,arr);
    
        if(arr['X'-65]>0)
            get_num("SIX",6,output,arr);
    
        if(arr['G'-65]>0)
            get_num("EIGHT",8,output,arr);

    
         if(arr['Z'-65]> 0)
            get_num("ZERO",0,output,arr);


          if(arr['O'-65] > 0 )
            get_num("ONE",1,output,arr);

         if(arr['R'-65] > 0 )
             get_num("THREE",3,output,arr);

         if(arr['F'-65]> 0 )
            get_num("FIVE",5,output,arr);

          if(arr['S'-65] > 0 )
             get_num("SEVEN",7,output,arr);
        
            if(arr['N'-65]> 0)

                 get_num("NINE",9,output,arr);
        

        std::sort(output.begin(),output.end(), std::less<int>());

        cout<<"Case #"<<t+1<<": ";
        for(vector<int>::iterator it2 = output.begin();it2<output.end();++it2){
            cout<<*it2;
        }

        if(t<T-1)
        cout<<endl;




    }
}


void get_num(string str,int i,vector<int> &output, int * arr){

     vector<int> tmp;
    
     for (int k = 0 ;k <26;++k){
        tmp.push_back(arr[k]);
        }
    
    int min=1000000;
    for(string::iterator it1 = str.begin(); it1< str.end(); ++it1 ) {
        if( min > 0 && tmp[(*it1-65)] < min ){
            min = tmp[(*it1-65)];
            --tmp[(*it1-65)];
        }
    }

    if(min > 0){
        for(int l = 0 ;l<min;++l){
            output.push_back(i);
        }

        for(string::iterator it1 = str.begin(); it1< str.end(); ++it1 ) {
            arr[(*it1-65)] -= min;

        }
    }
}

