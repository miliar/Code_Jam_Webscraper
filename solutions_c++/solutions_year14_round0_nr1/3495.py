#include <iostream>
#include <fstream>
using namespace std;
int main(){
    ifstream in("A-small-attempt2.in");
    //ifstream in("input.txt");
    ofstream out("A-small-attempt2.out");
    int cases;
    in>>cases;
    int i=0;
    int j=0;
    int k=0;
    int row1 = 0;
    int row2 = 0;
    int row1data[4];
    int row2data[4];
    int temp;
    int result;
    int count;
    while(i<cases)
    {
        count =0;
        in>>row1;
        for(j=0; j<4; j++){
            for(k=0; k<4; k++){
                if(j == row1-1){
                    in>>row1data[k];
                }else{
                    in>>temp;   
                }
            } 
        }
        
        in>>row2;
        for(j=0; j<4; j++){
            for(k=0; k<4; k++){
                if(j == row2-1){
                    in>>row2data[k];
                }else{
                    in>>temp;   
                }
            } 
        }
        
        for(j=0; j<4; j++){
            for(k=0; k<4; k++){
                if(row1data[j]== row2data[k]){
                    result = row1data[j];
                    count=count+1;
                }
                //cout<<"Count = "<<count<<endl;
                if(count==2){
                    break;   
                }
            } 
        }
        
        if(count==0){
            out<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;    
        }else if(count==1){
            out<<"Case #"<<i+1<<": "<<result<<endl;   
        }else{
            out<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;   
        }
        /*cout<<"Data============="<<endl<<endl;
        cout<<row1<<endl;
        for(j=0; j<4; j++){
            cout<<row1data[j]<<"    ";   
        }
        cout<<endl;
        cout<<row2<<endl;
        for(j=0; j<4; j++){
            cout<<row2data[j]<<"    ";   
        }
        cout<<endl;
        */
        i++;
    }
    
    //system("pause");
    return 0;
    
}
