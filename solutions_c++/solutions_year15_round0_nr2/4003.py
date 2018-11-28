#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int superf(vector<int> vec){
    if(vec.front()<=3){
        return vec.front();
    }
    else if(vec.front()<9){
       int x=vec.front()/2, y=vec.front()-x;
       pop_heap (vec.begin(),vec.end()); vec.pop_back();
       vec.push_back(x);
       vec.push_back(y);
       push_heap (vec.begin(),vec.end());
       return min(1+ superf(vec), x+y);

    }

        pop_heap (vec.begin(),vec.end()); vec.pop_back();
        vector<int> v2(vec);
        vec.push_back(3);vec.push_back(6);
        v2.push_back(4);v2.push_back(5);
        push_heap(vec.begin(), vec.end());
        push_heap(v2.begin(), v2.end());
        return min(min(9,1+superf(vec)),1+superf(v2));
  }

int main () {

  int num_test;
  cin>>num_test;

  int  result [100];

  for( int i=0; i< num_test; i++){
    int D, temp;
    cin>>D;

    vector<int> v;

    for(int j=0; j< D;j++)
    {
        cin>>temp;
        v.push_back(temp);
    }
    
    make_heap (v.begin(),v.end());

    result[i]=superf(v);

  }

  for(int i=0; i<num_test; i++){
    cout<<"Case #"<<(i+1)<<": "<<result[i]<<endl;
  }

  return 0;
}