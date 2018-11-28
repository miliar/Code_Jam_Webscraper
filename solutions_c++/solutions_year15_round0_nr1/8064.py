#include <fstream>
#include <iostream>


using namespace std;

int friends(string people){
    
    int f = 0;
    unsigned int p = 0;
    
    for(unsigned int i=0; i<people.size(); i++) {
        //cout << "\t" << f << " " << p << " " << i << " " << people[i] << "\n";
        if( p >= i ){
            p += people[i] - '0';
        } else if( p < i){
            int t = i-p;
            f += t;
            p += t + (people[i] - '0');
        }
    }
    
    
    return f;
}


int main(){
    
    //ifstream in("input.txt");
    //ifstream in("A-small.in");
    ifstream in("A-large.in");
    ofstream out("output.txt");
    
    int T;
    in >> T;
    
    for(int i=0; i<T; i++) {
        
        int Smax;
        in >> Smax;
        string people;
        
        getline(in, people);
        people = people.substr(1, people.size());
        
        //cout << people << "\n";
        
        out << "Case #" << (i+1) << ": " << friends(people) << "\n";
        cout << "Case #" << (i+1) << ": " << friends(people) << "\n";
    }
    
    return 0;
}
