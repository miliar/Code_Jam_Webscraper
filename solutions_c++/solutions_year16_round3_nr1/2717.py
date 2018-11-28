#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

class CompareDist
{
        public:
                    bool operator()(pair<int,char> n1,pair<int,char> n2) {
                                    return n1.first>n2.first;
                                        }
};

int main(){
    int test,n,temp;
    cin >> test; 
    for(unsigned t = 1;t <= test;t++){
        priority_queue<pair<int,char> > mypq;
        cin >> n;
        int sum = 0;
        for(unsigned int i=0;i<n;i++){ cin >> temp ; mypq.push(make_pair(temp,'A'+i));sum += temp;} 
        cout << "Case #" << t << ":";
        while(!mypq.empty()){
            pair<int,char> f1,f2;
            f1 = mypq.top(); mypq.pop();
            //cout << mypq.size() <<" "<<sum << " "<< f1.second ;
            if(!mypq.empty()){
                    f2 = mypq.top();mypq.pop();
                    if( f2.first > (sum -min(f1.first,2)) /2 ) {
                            f2.first--;
                            f1.first--;
                            sum -=2;
                            cout << " "<< f1.second << f2.second ;
                            if (f1.first > 0) mypq.push(f1);
                            if (f2.first > 0) mypq.push(f2);
                    }
                    else{
                            if( f1.first >= 2){ sum -=2 ;f1.first -= 2;cout << " "<< f1.second << f1.second ;}
                            else{ sum--;f1.first--;cout << " "<< f1.second ;}
                            if (f1.first > 0) mypq.push(f1);
                            mypq.push(f2);
                    }
            }
            else {
                if( f1.first >= 2){ sum -=2 ;f1.first -= 2;cout << " "<< f1.second << f1.second ;}
                else{ sum--;f1.first--;cout << " "<< f1.second ;}
                if (f1.first > 0) mypq.push(f1);
            } 
        //cout << "\n";
        }
        cout << "\n";
    }
    return 0;

}
