#include <iostream>;
#include <fstream>;
#include <set>;
#include <vector>;
using namespace std;
int main(){
    
    ifstream in("A-Small.in");
    ofstream out("A-Small.out");
    int tests;
    in>>tests;
    for(int i=0;i<tests;i++){
            int ans1,ans2;
            vector<int> repeated;
            in>>ans1;
            set<int> s;
            for(int j=0;j<4;j++){
                    for(int g=0;g<4;g++){
                            int num;
                            in>>num;
                            if(j==ans1-1){
                                          s.insert(num);
                            }        
                    }        
            }
            in>>ans2;
            for(int j=0;j<4;j++){
                    for(int g=0;g<4;g++){
                            int num;
                            in>>num;
                            if(j==ans2-1){
                                          int size=s.size();
                                          s.insert(num);
                                         
                                          if(s.size()==size){
                                                             
                                              repeated.push_back(num);                   
                                          }
                            }        
                    }        
            }
            string answer="Bad magician!";
            if(repeated.size()==0){
                answer="Volunteer cheated!";                                                                    
            }else if(repeated.size()==1){
                out<<"Case #"<<(i+1)<<": "<<repeated[0]<<"\n";
                continue;   
            }
            
            out<<"Case #"<<(i+1)<<": "<<answer<<"\n";                    
    }
    
    
}
