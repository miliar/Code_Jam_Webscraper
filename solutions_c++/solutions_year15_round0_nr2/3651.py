#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;

int main(){
    ifstream fin("input_st.txt");
    ofstream fout("js.txt");
    int num = 1;
    string name, inpt, prevname;
    string lng, lan;
    int id = 0;
    fout<<"var clusterline6 = [];"<<endl;
//    getline(fin, inpt);
    while(getline(fin, inpt)){
        if(inpt[0] < '6')
            continue;
        if(inpt[0] != '6')
            break;
        int i = 2;
        name = "";
        for(; i < inpt.size(); i ++){
            if(inpt[i] == '	')
                break;
            name += inpt[i];
        }
        if(id == 0){
            fout<<"var cline"<<num<<" = ["<<endl;
            id ++;
        }else if(name != prevname){
            fout<<endl;
            fout<<"];"<<endl;
            fout<<"clusterline6.push(cline"<<num<<");"<<endl;
            num ++;
            fout<<"var cline"<<num<<" = ["<<endl;
        }else if(name == prevname){
            fout<<","<<endl;
        }
        prevname = name;
//        cout<<name<<endl;
        while(inpt[i] != '-')
            i ++;
        lng = "";
        for(; i < inpt.size(); i ++){
            if(inpt[i] == '.' || (inpt[i] >= '0' && inpt[i] <= '9') || inpt[i] == '-')
                lng += inpt[i];
            else
                break;
        }
//        cout<<lng<<" ";
        i ++;
        lan = "";
        for(; i < inpt.size(); i ++){
            lan += inpt[i];
        }
   //     cout<<lan<<endl;
        fout<<"new google.maps.LatLng("<<lan<<","<<lng<<")";
    }
    fout<<endl;
    fout<<"];"<<endl;
    fout<<"clusterline6.push(cline"<<num<<");"<<endl;
    fin.close();
    fout.close();
    return 0;
}

/*
int main(){
    ifstream fin("input_sec.txt");
    ofstream fout("jssec.txt");
    int num = 1;
    string ids, snor;
    string lng, lan;
    int id = 0;
    fout<<"var arterialsectionMarker=[];"<<endl;
    fout<<"var arterialSectionLoc = [ "<<endl;
//    getline(fin, inpt);
    while(fin>>ids>>lng>>lan>>snor){
        if(id)
            fout<<","<<endl;
        fout<<"['"<<ids<<"',"<<lan<<","<<lng<<",'"<<snor<<"']";
        id ++;
    }
    fout<<endl;
    fout<<"];"<<endl;
    fin.close();
    fout.close();
    return 0;
}*/
