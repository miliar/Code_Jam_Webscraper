#include<iostream>
#include<fstream>
#include <vector>

using namespace std;

int main() {

 ifstream myReadFile;
 ofstream outfile;
 myReadFile.open("D-large.in");
 outfile.open("out.out");
 int casos, piezas, final;
 float num;
vector<float> Naomi, Ken, Naomi1, Ken1;
 if (myReadFile.is_open()) {
    
    myReadFile >> casos;
    //cout << casos;
    for(int i=0; i < casos; i++){
        myReadFile >> piezas;
        for(int j=0;j<piezas;j++){
            myReadFile >> num;
            Naomi.push_back(num);    
        }
        for(int j=0;j<piezas;j++){
            myReadFile >> num;
            Ken.push_back(num);    
        }
        
        cout << Naomi[0] << endl;
        
        
        float aux;
        for(int m=0;m<piezas;m++){
        for(int j=0;j<piezas-1;j++){
            if(Naomi[j]<Naomi[j+1]){
                aux=Naomi[j];
                Naomi[j]=Naomi[j+1];
                Naomi[j+1]=aux;
            }
            if(Ken[j]<Ken[j+1]){
                aux=Ken[j];
                Ken[j]=Ken[j+1];
                Ken[j+1]=aux;
            }
        }
        }
        Naomi1=Naomi;
        Ken1=Ken;
        for(int j=0;j<piezas;j++){
            cout << Naomi1[j] << " ";    
        }
        cout << endl;
        for(int j=0;j<piezas;j++){
            cout << Ken1[j] << " ";    
        }
        cout << endl;
        final=piezas-1;
        
        
        int score=0;
        while(Naomi.size()>0){
            if(Naomi[final]<Ken[final]){
                 Ken.erase (Ken.begin());   
                 Naomi.erase (Naomi.begin()+final);
                 final--;
            }else if(Naomi[final]>Ken[final]){
                Ken.erase (Ken.begin()+final);   
                 Naomi.erase (Naomi.begin()+final);
                 final--;
                score ++;
            }
        }
        
        final=piezas-1;
        int score2=0;
        while(Ken1.size()>0){
            if(Naomi1[0]>Ken1[0]){
                Ken1.erase (Ken1.begin()+final);   
                 Naomi1.erase (Naomi1.begin());
                 final--;
                 score2++;
            }else if(Naomi1[0]<Ken1[0]){
                Ken1.erase (Ken1.begin());   
                 Naomi1.erase (Naomi1.begin());
                 final--;
            }
        }
        
        outfile << "Case #" << i+1 << ": " << score << " " << score2;
        if(i!=casos-1)outfile << endl;
        
        Naomi.clear();
        Ken.clear();
    }   
}
myReadFile.close();
system("pause");
return 0;
}
