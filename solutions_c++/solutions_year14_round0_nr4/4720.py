#include<iostream>
#include<vector>
#include<string.h>
#include<float.h>
using namespace std;
//-------------------------------
//sorting
//-------------------------------
vector<double> NLogNInsertionSort(vector<double> input)
{
    int left,right,middle,position;
    for(int ii=1;ii<input.size();ii++){ //N
        double key=input[ii];
        int jj=ii-1;
        position=-1;
        if((input[0]-key)>=DBL_EPSILON)
            position=0;
        else if((input[jj]-key)>=DBL_EPSILON){
            left=0;
            right=jj;
            while(right-left>1){    //logN
                middle=(left+right)/2;
                if(key>=input[middle])
                    left=middle;
                else
                    right=middle;
            }
            position=left+1;
        }
        if(position>=0){
            memmove((void*)&input[position+1],(void*)&input[position],(ii-position)*sizeof(double)/sizeof(char));
            input[position]=key;
            
        }
    }
    return input;
}
//----------------------
//  find the mere large one
//----------------------
int findTheMereLargeOne(vector<double> ken, double key, vector<int> kenMap){
    int position=-1;
    int left,right,middle;
    left=0;right=ken.size()-1;
    if((ken[0]-key)>=DBL_EPSILON)
        position=0;
    else{
        while(right-left>1){
            middle=(left+right)/2;
            if(key-ken[middle]>DBL_EPSILON)
                left=middle;
            else if(ken[middle]-key>DBL_EPSILON)
                right=middle;
        }
        position=left+1;
        
    }
    if(kenMap[position]==1){
        int ii=position;
        while(kenMap[ii]==1)
            ii++;
        position=ii;
        if(ii>=ken.size())
            position=-1;
    }
    if(key>ken[ken.size()-1])
        position=-1;
    return position;
}

//----------------------
//  Play with honor
//----------------------
int playWithHonor(vector<double> naomi, vector<double> ken){
    int point=0;
    vector<double> sortedKen=NLogNInsertionSort(ken);
    vector<int> kenMap(ken.size());
    for(int ii=0;ii<ken.size();ii++){
        double temp=naomi[ii];
        int position=findTheMereLargeOne(sortedKen,temp, kenMap);
        if(position!=-1){
            kenMap[position]=1;
            //cout<<"kenscore with position of "<<position<<endl;
            point++;
        }else{
            int jj=0;
            for(jj=0;jj<ken.size();jj++){
                if(kenMap[jj]==0){
                    kenMap[jj]=1;
                    break;
                }
            }
            position=jj;
        }
        //cout<<"Naomi: "<<temp<<" Ken: "<<sortedKen[position]<<endl;
    }
    
    return sortedKen.size()-point;
}
//----------------------------------
//  Cheated Play
//----------------------------------
int cheatedPlay(vector<double> naomi, vector<double> ken){
    int point=0;
    vector<double> sortedNaomi=NLogNInsertionSort(naomi);
    vector<double> sortedKen=NLogNInsertionSort(ken);
    int headNaomi=0;
    int headKen=0;
    int tailKen=sortedKen.size()-1;
    while(headNaomi!=(naomi.size())){
        if(sortedNaomi[headNaomi]<sortedKen[headKen]){
            headNaomi++;
            tailKen--;
        }else if((sortedNaomi[headNaomi]-sortedKen[headKen]>DBL_EPSILON)){
            headNaomi++;
            headKen++;
            point++;
        }
    }
    return point;
}
//----------------
//main
//----------------
int main(){
    FILE* inputFile=fopen("D-large.in.txt","r");
    //FILE* inputFile=fopen("inputTemp.txt","r");
    FILE* outputFile=fopen("output.txt","a+");
    int iterator;
    fscanf(inputFile,"%d",&iterator);
    for(int ii=1;ii<=iterator;ii++){
        vector<double> naomi;
        vector<double> ken;
        int size;
        fscanf(inputFile,"%d",&size);
        for(int jj=0;jj<size;jj++){
            double temp;
            fscanf(inputFile,"%lf",&temp);
            naomi.push_back(temp);
        }
        for(int jj=0;jj<size;jj++){
            double temp;
            fscanf(inputFile,"%lf",&temp);
            ken.push_back(temp);
        }
        int point=cheatedPlay(naomi,ken);
        int honorPoint=playWithHonor(naomi,ken);
        //printf("Case #%d: %d %d\n",ii,point,honorPoint);
        fprintf(outputFile,"Case #%d: %d %d\n",ii,point,honorPoint);
    }
    return 0;
}