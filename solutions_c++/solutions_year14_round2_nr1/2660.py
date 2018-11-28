/* 
 * File:   main.cpp
 * Author: Shiva Prasad Goud Bandari <bshivagoud@gmaill.com>
 *
 * Created on 3 May, 2014, 9:17 PM
 */

#include <iostream>

using namespace std;

string process_string(string str, unsigned int * repeats){
    string s;
    s.push_back(str[0]);
    
    for(int j=0;j<100;j++){
        repeats[j]=0;
    }
    
    for(int i=1,j=0;i<str.size();i++){
        if(str[i]==str[i-1])
            repeats[j]++;
        else{
            s.push_back(str[i]);
            j++;
        }   
    }
    
    return s;
};

int main(int argc, char** argv) {
    
    unsigned int T,N,loses=0;
    
    string modelstring;

    cin >> T;
    for(int t=1;t<=T;t++) {
        cin>>N;
        
        string line,pline;
        unsigned int repeats[100][100];
        for(int i=0;i<N;i++){
            cin>>line;
            line = process_string(line,repeats[i]);
            if(i==0)
                pline = line;
            else{
                if(pline.compare(line) != 0){
                    loses=1;
                    break;
                }
            }
        }
        
        
        int n=0;
        if(loses==1){
            cout << "Case #"<<t<<": Fegla Won\n";
            loses=0;
        }
        else{
            for(int j=0;j<100;j++){
                int temp = repeats[1][j]-repeats[0][j];
                if(temp<0)
                    temp = -temp;
                n+=temp;
            }        
            cout << "Case #"<<t<<": "<<n<<endl;
        }
    }

    return 0;
}