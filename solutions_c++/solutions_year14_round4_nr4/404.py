//
//  main.cpp
//  GCJ14_R2_D
//
//  Created by Ningchen Ying on 5/31/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <cstring>
using namespace std;

struct Node{
    Node* next[30];
}tot_case[101000];

int id;

Node* newnode(){
    memset(tot_case[id].next,0,sizeof(tot_case[id].next));
    return &tot_case[id++];
}

struct Trie{
    int cnt;
    Node *root;
    void clear(){
        cnt = 0;
        root = newnode();
    }
    
    void insert(char *it){
        cnt++;
        Node *p = root;
        for (; *it; it++){
            int num = (*it)-'A';
            if (p->next[num]==NULL) p->next[num] = newnode();
            p = p->next[num];
        }
    }
    
};

char ync[20][101];

void solve(int M,int N,int ca){
    int tot = 1;
    for (int i = 0;i<M;i++){
        tot*=N;
    }
    //cout<<tot<<endl;
    Trie nying[10];
    int ans = 0, cn_ans = 0,tmp;
    for (int size_id = 0; size_id<tot; size_id++){
        id = 0;
        tmp = size_id;
        for (int i = 0;i<N;i++){
            nying[i].clear();
        }
        
        for(int i = 0;i<M;i++){
            int j = tmp%N;
            tmp = tmp / N;
            nying[j].insert(ync[i]);
        }
        
        for(int i =0;i<N;i++){
            if (nying[i].cnt==0) id--;
        }
        int tmp_a = id;
        if (tmp_a > ans){
            cn_ans = 1;
            ans = tmp_a;
        }else if (tmp_a==ans) cn_ans++;
    }
    printf("Case #%d: %d %d\n", ca, ans, cn_ans);
}

int main(int argc, const char * argv[])
{
    freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_D/GCJ14_R2_D/D-small-attempt0.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_D/GCJ14_R2_D/D-small-attempt0.out","w", stdout);
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_B/GCJ14_R2_B/B-large.in","r",stdin);
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_B/GCJ14_R2_B/B-large.out","w", stdout);
    int T,M,N;
    cin>>T;
    for (int ca = 1; ca<=T; ca++){
        scanf("%d%d",&M,&N);
        for (int i = 0;i < M;i++){
            //scanf("%s",ync[i]);
            cin>>ync[i];
            //cout<<i<<" "<<M<<endl;
            //cout<<ync[i]<<endl;
        }
        solve(M,N,ca);
    }
}

