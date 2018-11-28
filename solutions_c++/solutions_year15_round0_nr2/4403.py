//
//  Pancake.cpp
//  
//
//  Created by Jefvin Viriya on 11/4/15.
//
//

#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int doSecondEat(vector<int>);
int doSpecial(vector<int>);
int doEat(vector<int>);

int t;
int d;
int pOrang[1005];

bool cekZero(vector<int> listPancake){
    for(int i=0;i<listPancake.size();i++){
        if(listPancake[i]>0)return false;
    }
    return true;
}

int doSecondEat(vector<int> listPancake){
    if(cekZero(listPancake)){
        return 0;
    }
    for(int i=0;i<listPancake.size();i++){
        listPancake[i]--;
    }
    /*printf("eat ");
    for(int i=0;i<listPancake.size();i++){
        printf("%d ",listPancake[i]);
    }
    printf("\n");*/
    int value1 = 1+doSecondEat(listPancake);
    int value2 = 1+doSpecial(listPancake);
    return min(value1,value2);
}

int doSpecial(vector<int> listPancake){
    if(cekZero(listPancake)){
        return 0;
    }
    int idxMax = 0;
    for(int i=1;i<listPancake.size();i++){
        if(listPancake[i]>listPancake[idxMax]){
            idxMax = i;
        }
    }
    if(listPancake[idxMax]>1){
        int minimum = 999999;
        for(int i=2;i<(listPancake[idxMax]/2)+1;i++){
            listPancake.push_back(i);
            //int x = listPancake[idxMax];
            //printf("%d ",listPancake[idxMax]);
            
            listPancake[idxMax]-=i;
//            bool print=false;
//            if(listPancake.size()==2 && listPancake[0]==6 && listPancake[1]==3){
//                printf("abc\n");
//                print = true;
//            }
            int value1 = 1+doSecondEat(listPancake);
            int value2 = 1+doSpecial(listPancake);
//            if(print)printf("%d sda\n",value2);
            minimum = min(minimum,value1);
            minimum = min(minimum,value2);
            listPancake.pop_back();
            listPancake[idxMax]+= i;
            //int y = listPancake[idxMax];
            //printf("%d %d aa\n",x,y);
        }
        /*printf("special: ");
        for(int i=0;i<listPancake.size();i++){
            printf("%d ",listPancake[i]);
        }
         printf("\n");*/
        //if(listPancake[0]==pOrang[0])printf("%d dasdasas\n",minimum);
        return minimum;
    }else{
        return 1;
    }

    
}

int doEat(vector<int> listPancake){
    if(cekZero(listPancake)){
        return 0;
    }
    //printf("b\n");
    return min(doSecondEat(listPancake),doSpecial(listPancake));
}

int main(){
    
    vector<int> listPancake;
    int i,j,k;
    
    scanf("%d",&t);
    
    for(int c=1;c<=t;c++){
        scanf("%d",&d);
        listPancake.clear();
        for(i=0;i<d;i++){
            scanf("%d",&pOrang[i]);
            listPancake.push_back(pOrang[i]);
        }
        printf("Case #%d: %d\n",c,doEat(listPancake));
        
        
        
    }
    
    return 0;
}