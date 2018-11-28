#include <stdio.h>
#include <iostream>
int twos(long long int input){
    long long int trail=1;
    int power=0;
    while(trail<input){
        trail=trail*2;
        power++;
        if(power>100){trail=input;power=-1;}
    }
    if (trail!=input){power--;}
    return(power);
}
int check(long long int input){
    long long int trail=input;
    long long int temp;
    int power=1;
    while(trail>2){
        temp=trail/2;
        if(temp*2!=trail){trail=0;power=-1;}else{trail=temp;}
    }
    return(power);
}
long long int common(long long int P1,long long int Q1){
long long int factor=1;

for (long long int a=1;a<(P1+1);a++){
if((Q1%a==0)&&(P1%a==0)){factor=a;}
}

return(factor);
}

int main (){


    int length=0;
    int outputs[100];
    int maxl=0;
    long long int P=0;
    long long int Q=0;
    long long int factor;
    int top;
    int bot;
    char fix;

    //read data
        // change seperator
        FILE* fixer;
        fixer = fopen ("A-small-attempt0 (2).in","r");//enter file name
        FILE * source;
        source = fopen ("test1.in","w");//enter file name



    do {
      fix = fgetc (fixer);
      if (fix == '/'){fputc(' ',source);}else{fputc(fix,source);}
    } while (fix != EOF);
    fclose (fixer);
    fclose (source);

source = fopen ("test1.in","r");//enter file name

        //read date
        fscanf(source,"%i",&maxl);
        while(length<maxl){
            fscanf(source,"%lli",&P);
            fscanf(source,"%lli",&Q);
            std::cout<<P<<"\\"<<Q<<"\n";
            factor=common(P,Q);


            Q=Q/factor;
            P=P/factor;
            std::cout<<P<<"\\"<<Q<<"\n";
            if(check(Q)==-1){outputs[length]=-1;std::cout<<"error"<<"\n";}
            else{
                top=twos(P);
                bot=twos(Q);
                outputs[length]=bot-top;
                std::cout<<bot<<"-"<<top<<"="<<outputs[length]<<"\n";
            }


            length++;
        }

        fclose(source);





    //write output

        source = fopen ("output.in","w");
        for(int a=0;a<maxl;a++){

            if((outputs[a]<0)||outputs[a]>40){
                fprintf(source,"Case #%d: impossible\n",(a+1));
            }else{
                fprintf(source,"Case #%d: %d\n",(a+1),outputs[a]);
            }


        }
        fclose(source);

    return 0;
}
