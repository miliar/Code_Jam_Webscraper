#include<iostream>
#include<cstring> 
#include<string>
#include<fstream>
#include<sstream>
#include<cstdlib>

using namespace std;
void set_bits(char * a,int len,unsigned long long int k);
bool is_all_ones(char * a, int len);

int main(int argc, char ** argv){

    if(argc <2)
    {
        cerr<<"No input file provided"<<endl;
        exit(EXIT_FAILURE);
    }

    ifstream infile(argv[1]);
    istringstream ss;    

    int T;
    unsigned long long int N;    

    infile>>T;

    string ans;
    for(int i=0;i<T;++i){
        char a[10]; 
        memset(a, 0, 10);  
        infile>>N;

        if(N == 0){
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA";
        }else{

            unsigned long long int counter=1,lnum=N; 

            set_bits(a,10,N);

            while(!is_all_ones(a,10)){
                ++counter;
                lnum=N*counter;
                set_bits(a,10,lnum);
            }

            cout<<"Case #"<<i+1<<": "<<lnum;
        }
        if(i<T-1)
            cout<<endl;       
    }

}

void set_bits(char * a,int len,unsigned long long int k){
    while(k!=0){
        if(k%10 <len)
            a[k%10] = 1;    
        k = k/10; 
    }
}

bool is_all_ones(char * a, int len){
    bool res=true;
    for(int k = 0;k<len;++k){
        if (a[k] == 0) {
            res = false;
            break;
        }
    }
    return res;
}
