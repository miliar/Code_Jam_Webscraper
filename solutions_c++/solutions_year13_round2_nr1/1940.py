#include <iostream>
#include <algorithm>

using namespace std;

int mote(int *array,int val, int i, int N); 
int main(){
    int T;
    cin>>T;
    int i;
    for(i=0;i<T;i++){
        int mot,SIZE;
        cin>>mot;
        cin>>SIZE;
        int *array = new int[SIZE];
        for(int k=0;k<SIZE;k++){
            cin>>array[k];
        }
        sort(array, array + SIZE);     
        int ret = mote(array,mot,0,SIZE);
        cout<<"Case #"<<i+1<<": "<<ret<<endl;
        delete [] array;
    }     
}

int mote(int *array,int val, int i, int N){
    if(i==N){
        return 0;
    }
    if(val > array[i]){
        return 0+mote(array,val+array[i],i+1,N);
    }
    else{
        if( val != 1){    
            int v2 = 1+mote(array,2*val-1,i,N); 
            int v1 = N-i;     
            if(v1 <= v2){
                return v1;
            }
            else{
                return v2;
            }
       }
       else{
            return N-i;
       }          
    }    
}                    
         
