#include<stdio.h>
#include<iostream>
#include<memory.h>
#include<queue>


using namespace std;


int countSlice(deque<int> dq , int max_top){
    int cnt = 0;
    int len = dq.size();
    for(int i=0;i<len;++i){
        if(dq[i] > max_top)
            cnt += dq[i]/max_top - 1 + (dq[i]%max_top != 0);
    }
    
    return cnt;
}

int main(){
    
    freopen("in.txt", "r", stdin);
    
    
    int T,n,v;
    cin>>T;
    
    for(int i=0;i<T;++i){
        priority_queue<int> pq;
        deque<int> dq;
        cin>>n;
        for(int j=0;j<n;++j){
            cin>>v;
            pq.push(v);
            dq.push_back(v);
        }
        
        int top = pq.top();
        
        int thres = pq.top();
        int min_top = pq.top();
        int cnt = 1;
        while(cnt < thres){
            int t = pq.top();
            
            
            int half = t/2;
            pq.push(half);
            pq.push(t - half);
            pq.pop();
            
            if(pq.top() + cnt < thres){
                thres = pq.top() + cnt;
                min_top = pq.top();
            }
            
            ++cnt;
        }
        
        thres = top;
        
        for(int j=1;j<=top;++j){
            int tmp = countSlice(dq,j);
            //cout<<j<<"-"<<tmp<<endl;
            
            if(tmp + j < thres )
                thres = tmp + j;
        }
        
        
        cout<<"Case #"<<(i+1)<<": "<<thres<<endl;
        
        
    }
    
    return 0;
}
