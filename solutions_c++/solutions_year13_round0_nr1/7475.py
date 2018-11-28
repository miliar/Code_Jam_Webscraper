#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int main(){
    ofstream file("real.txt",ios_base::app);
    int t ;
    char bl ;
    cin >> t ;
    for(int i=1;i<=t;i++) {
        char input[4];
        char p[16];
        int j=0;
        if(i>=2){

             scanf("%c",&bl);
        }
        for(int x=0;x<4;x++){
            scanf("%s",input);
            for(int y=0;y<4;y++)
                p[j++]=input[y];
        }
        if((p[0]=='T'||p[0]=='X')&&(p[1]=='T'||p[1]=='X')&&(p[2]=='T'||p[2]=='X')&&(p[3]=='T'||p[3]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[0]=='T'||p[0]=='O')&&(p[1]=='T'||p[1]=='O')&&(p[2]=='T'||p[2]=='O')&&(p[3]=='T'||p[3]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else if((p[4]=='T'||p[4]=='X')&&(p[5]=='T'||p[5]=='X')&&(p[6]=='T'||p[6]=='X')&&(p[7]=='T'||p[7]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[4]=='T'||p[4]=='O')&&(p[5]=='T'||p[5]=='O')&&(p[6]=='T'||p[6]=='O')&&(p[7]=='T'||p[7]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else  if((p[8]=='T'||p[8]=='X')&&(p[9]=='T'||p[9]=='X')&&(p[10]=='T'||p[10]=='X')&&(p[11]=='T'||p[11]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[8]=='T'||p[8]=='O')&&(p[9]=='T'||p[9]=='O')&&(p[10]=='T'||p[10]=='O')&&(p[11]=='T'||p[11]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else if((p[12]=='T'||p[12]=='X')&&(p[13]=='T'||p[13]=='X')&&(p[14]=='T'||p[14]=='X')&&(p[15]=='T'||p[15]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[12]=='T'||p[12]=='O')&&(p[13]=='T'||p[13]=='O')&&(p[14]=='T'||p[14]=='O')&&(p[15]=='T'||p[15]=='O'))
            file << "Case #"<<i<<": O won"<<endl;


        else if((p[0]=='T'||p[0]=='X')&&(p[4]=='T'||p[4]=='X')&&(p[8]=='T'||p[8]=='X')&&(p[12]=='T'||p[12]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[0]=='T'||p[0]=='O')&&(p[4]=='T'||p[4]=='O')&&(p[8]=='T'||p[8]=='O')&&(p[12]=='T'||p[12]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else if((p[1]=='T'||p[1]=='X')&&(p[5]=='T'||p[5]=='X')&&(p[9]=='T'||p[9]=='X')&&(p[13]=='T'||p[13]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[1]=='T'||p[1]=='O')&&(p[5]=='T'||p[5]=='O')&&(p[9]=='T'||p[9]=='O')&&(p[13]=='T'||p[13]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else  if((p[2]=='T'||p[2]=='X')&&(p[6]=='T'||p[6]=='X')&&(p[10]=='T'||p[10]=='X')&&(p[14]=='T'||p[14]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[2]=='T'||p[2]=='O')&&(p[6]=='T'||p[6]=='O')&&(p[10]=='T'||p[10]=='O')&&(p[14]=='T'||p[14]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else if((p[3]=='T'||p[3]=='X')&&(p[7]=='T'||p[7]=='X')&&(p[11]=='T'||p[11]=='X')&&(p[15]=='T'||p[15]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[3]=='T'||p[3]=='O')&&(p[7]=='T'||p[7]=='O')&&(p[11]=='T'||p[11]=='O')&&(p[15]=='T'||p[15]=='O'))
            file << "Case #"<<i<<": O won"<<endl;


         else if((p[0]=='T'||p[0]=='X')&&(p[5]=='T'||p[5]=='X')&&(p[10]=='T'||p[10]=='X')&&(p[15]=='T'||p[15]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[0]=='T'||p[0]=='O')&&(p[5]=='T'||p[5]=='O')&&(p[10]=='T'||p[10]=='O')&&(p[15]=='T'||p[15]=='O'))
            file << "Case #"<<i<<": O won"<<endl;
        else if((p[3]=='T'||p[3]=='X')&&(p[6]=='T'||p[6]=='X')&&(p[9]=='T'||p[9]=='X')&&(p[12]=='T'||p[12]=='X'))
            file << "Case #"<<i<<": X won"<<endl;
        else if((p[3]=='T'||p[3]=='O')&&(p[6]=='T'||p[6]=='O')&&(p[9]=='T'||p[9]=='O')&&(p[12]=='T'||p[12]=='O'))
            file << "Case #"<<i<<": O won"<<endl;

        else if((p[0]=='.') ||( p[1]=='.') || (p[2]=='.')||( p[3]=='.')||( p[4]=='.') ||( p[5]=='.') ||( p[6]=='.') ||
                ( p[7]=='.') || ( p[8]=='.') || ( p[9]=='.') || ( p[10]=='.') || ( p[11]=='.') || ( p[12]=='.') ||
                ( p[13]=='.') || ( p[14]=='.') || ( p[15]=='.') )
                file << "Case #"<<i<<": Game has not completed"<<endl;
        else
                file << "Case #"<<i<<": Draw"<<endl;



    }
    return 0 ;
}
