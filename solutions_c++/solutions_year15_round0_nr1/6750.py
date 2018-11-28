#include <iostream>
#include <vector>
using namespace std;

int main(){

  int casos;

  cin>>casos;

  for(int i=0; i < casos; i++){
    int timi;


    cin>> timi;
    string pal;
    cin>>pal;

    int total =0;
    int resp = 0;

    for(int j=0; j <= timi; j++){

        int num = pal[j] - '0';
        if(total >= j){
            total += num;
        }else{
            resp+= (j-total);
            total+= (j-total);
            total+= num;
        }

    }

    cout<<"Case #"<<i+1<<": "<<resp<<endl;
  }
    return 0;
}
