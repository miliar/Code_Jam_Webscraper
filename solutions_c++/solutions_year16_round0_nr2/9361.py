#include<iostream> 
#include<string>
#include<fstream>
#include<sstream>
#include<cstdlib>

using namespace std;

int main(int argc, char ** argv){

    if(argc <2)
    {
        cerr<<"No input file provided"<<endl;
        exit(EXIT_FAILURE);
    }

    ifstream infile(argv[1]);
    istringstream ss;    

    int N;
    string line;

    getline(infile,line);
    ss.str(line);
    ss.seekg(0,ss.beg);
    ss>>N;

    for(int i=0;i<N;++i){
        getline(infile,line);
        int opcount=0;
        if(line.length() == 1){
            //case when string length is 1        
            if(line == "-")
                ++opcount;
        }   
        else {
            char prev='\0';         
            char curr=*(line.begin());
            for(string::iterator it=line.begin()+1;it!=line.end();++it){

                if(curr == *it )
                    continue;
                else{
                    if(prev == '\0')
                    {   
                        prev = curr;
                        curr = *it;
                        continue; 
                    }
                    else{   

                        if(curr == '-' && prev == '+' ){
                            opcount += 2;
                        }
                        else if (curr == '+' && prev =='-' ){
                            opcount += 1;
                        }

                        prev = '+';
                        curr = *it;           
                    }                

                }
            }

			// 
						if(curr == '-' && prev == '+' ){
                            opcount += 2;
                        }
                        else if (curr == '+' && prev =='-' ){   //when input is ------+
                            opcount += 1;
                        }else if (curr== '-' && prev== '\0'){ //when input is all -ve
						   opcount +=1; 			
						}else if( curr == '+' && prev == '\0'){ //when input is all +ve 
							// do nothing 
						}
        }
        cout<<"Case #"<<i+1<<": "<<opcount;
        if(i!=N-1)
            cout<<endl;
    }

}
