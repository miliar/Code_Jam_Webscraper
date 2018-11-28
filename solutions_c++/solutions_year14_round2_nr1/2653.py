#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<vector> 
#include<algorithm> 

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int T;
    
    fin >> T;
    for (int t=0;t<T;t++ )
    {
        int N;
        fin >> N;
        
        bool F_win = false;
        vector<string> F_str;
        vector<vector<int> > F_num;
        
        for (int n=0;n<N;n++){
            
            string str;
            int charcount;
            vector<int> charnum;
            fin >> str;
            
            string::iterator p= str.begin();
            string::iterator q= p+1;
            charcount = 0;
            while ( q!= str.end() ){
                  if(*q == *p){
                        q = str.erase(q);
                        charcount++;
                  }
                  else{
                       charnum.push_back( charcount+1 );
                       charcount = 0;
                       p = q;
                       q = q+1;
                  }                  
            }
            charnum.push_back( charcount+1 );
            
            if (n>0){
                 if (str.compare(F_str[0]) !=0 ){
                    F_win = true;
                    break;
                 }
            }
            
            F_str.push_back(str); 
            F_num.push_back(charnum);
            
        }
        
        fout << "Case #" << t+1 << ": " ;
        
        // output here:
        if(F_win)
            fout << "Fegla Won";
        else{
            int MoveCount = 0;
            
            for (int i=0;i<F_str[0].size();i++){
                vector<int> tmpRepeat;
                
                for (int n=0;n<N;n++) {
                    tmpRepeat.push_back( F_num[n][i] );
                }
                sort(tmpRepeat.begin(),tmpRepeat.end() );
                
                for (int n=0;n<N;n++)
                    MoveCount+= abs( tmpRepeat[n] -tmpRepeat[N/2]);
                
            }             
            fout << MoveCount;
        }
         
        fout << endl;
       // for (int n=0;n<N;n++){
//            for (int i=0;i<F_str[n].size();i++)
//                fout << F_num[n][i] <<" ";
//            fout << endl;;
//        }
    }    
    
    fin.close();
    fout.close();
    
    return 0;
}
