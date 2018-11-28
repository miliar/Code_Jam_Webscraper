//
//  main.cpp
//  DeceitfulWar
//
//  Created by Yitao Liang on 14-4-12.
//  Copyright (c) 2014年 Yitao Liang. All rights reserved.
//

#include <iostream>
using namespace std;
struct Number{
    int flag;
    float value;
};
#include <vector>
#include <time.h>
void quickSort(vector<Number> &v,int start,int end);
void swap(Number &a, Number& b);
int main(){
    freopen("D-large.in.txt","r",stdin);
    freopen("D-large.out.txt","w",stdout);
    //freopen("d.in","r",stdin);
    int t,n,s,m,s1;
    m=0;
    cin>>t;
    Number number;
    vector <Number> v;
    srand((int)time(NULL));
    for (int i=1;i<=t;i++){
        cin>>n;
        for (int j=1;j>=0;j--){
            for (int k=0;k<n;k++){
                number.flag=j;
                cin>>number.value;
                v.push_back(number);
            }
        }
        quickSort(v,0,(int)v.size()-1);
        /*for (int j=0;j<=(int)v.size()-1;j++){
            cout<<v[j].value<<" ";
        }
        cout<<endl;*/
        s=n;
        s1=0;
        for (int j=(int)v.size()-1;j>=0;j--){
            if (v[j].flag){
                if (s1<0){
                    s+=s1;
                    s1=1;
                }else{
                    s1+=1;
                }
            }else{
                s1-=1;}
        }
        if (s1<0) s+=s1;
        cout<<"Case #"<<i<<": "<<s;
        
        
        s=0;
        s1=0;
        for (int j=(int)v.size()-1;j>=0;j--){
            if (v[j].flag){
                s1+=1;
            }else{
                if (s1>0) {
                    s+=s1;
                    s1=-1;
                }else{
                    s1-=1;
                }
            }
        }
        if (s1>0) s+=s1;
        cout<<" "<<s<<endl;
        v.clear();
        
    }
    
    return 0;
}


void quickSort(vector<Number> &v,int start,int end){
    int pivot;
    pivot=rand()%(end-start)+start;
    swap(v[pivot],v[start]);
    int i,j;
    i=start+1;
    j=end;
    while (true){
        while (v[j].value>v[start].value){
            j--;
        }
        while (v[i].value<v[start].value && i<j){
            i++;
        }
        if (i>=j) break;
        swap(v[i],v[j]);
    }
    if (v[start].value>v[j].value) swap(v[start],v[j]);
    if (start<j-1) quickSort(v,start,j-1);
    if (end>j+1) quickSort(v,j+1,end);
    
}

void swap(Number &a, Number& b){
    Number c;
    c=a;
    a=b;
    b=c;
}