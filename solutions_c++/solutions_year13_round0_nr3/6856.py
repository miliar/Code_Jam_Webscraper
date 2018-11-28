#include <iostream>
#include <math.h>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

bool is_fs(int nb);
bool is_pal(int nb);
int search_fs_in_interval(int a, int b);

int main()
{
    int t=0,a=0,b=0;

    //on ouvre le fichier et on lit T:
    //FILE* input = fopen("C-small-attempt0.in","r+");
    FILE* input,* output;
    input = fopen("input.in","r");
    output = fopen("output.txt","w+");

    if(input==NULL)
        std::cout<<"pbm ouverture fichier"<<std::endl;
    else{
        fscanf(input, "%d", &t);
    }

    //lecture de T:

    std::cout<<"t: "<<t<<std::endl;

    for(int i = 0; i < t ; i ++){
        fscanf(input, "%d %d", &a, &b);
        fputs("Case #",output);
        char* str = (char*)malloc(10*sizeof(char));
        str=itoa(i+1, str, 10);
        fputs(str,output);
        fputs(": ",output);
        fputs(itoa(search_fs_in_interval(a,b),str,10),output);

        if(i!=t-1)
            fputc('\n',output);
    }

    return 0;
}

bool is_fs(int nb){

    if(!is_pal(nb))
        return false;


    //2 on vérifie que nb est un carré et que son carré est un plaindrome

    int root = sqrt(nb);
    double rootd = sqrt(nb);

    if((root==rootd)&&(is_pal(root)))
        return true;

    return false;
}

bool is_pal(int nb){

    //1 on vérifie que nb est un palindrome----------------
    //std::cout<<"1/"<<std::endl;

    //on transforme nb en chaine de characteres:
    //on trouve la puissance de 10 maximale +1 tel que nb%10 != 0
    int k = 0;
    while(( nb/(int)pow(10,k)) !=0)
        k++;

    //std::cout<<"2/"<<std::endl;

    char* s =(char*)malloc(k*sizeof(char));
    char* ps = s;
    int nb_temp = nb;

    for(int i = k-1 ; i >=0 ; i --){
        int d = floor(nb_temp/(pow(10,i)));
        nb_temp = nb_temp-pow(10,i)*d;
        *ps = (char)(((int)'0') + d);
        ps++;
    }
    ps=s;

    /*
    while(ps-s<k){
        std::cout<<*ps<<std::flush;
        ps++;
    }*/

    //si k est impaire on fait (k-1)/2 itérations
    //si k est paire on fait k/2 itérations

    int nb_it = (k%2==0?k/2:(k-1)/2);
    char* ps0 = s, *ps1 = s+k-1;

    /*std::cout<<"*ps0: "<<*ps0<<std::endl;
    std::cout<<"*ps1: "<<*ps1<<std::endl;
    std::cout<<nb_it<<std::endl;*/

    bool cont = true;
    while( (nb_it>0) && (cont==true) ){

        if(*ps0==*ps1){
            ps0++;
            ps1--;
            nb_it--;
        }
        else
            cont=false;
    }

    if(cont == false)   //si cont est false c'est que ce n'est pas un palindrome, sinon c'est que s'en est un
        return false;

    return true;
}


int search_fs_in_interval(int a, int b){
    int cpt = 0;    //compte le nombre de fair and squares dans l'interval [a,b]

    for(int i = a ; i <= b ; i++){
        if(is_fs(i))
            cpt++;
    }

    return cpt;
}
