#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;
/*
 All rights reserved
 Made by MQ 2016.4.7
*/
/*
 2016.3.31 需要解决的问题：
 1) expression，factor，item三者之间的关系需要厘清（左递归消除，具体得到的产生式见后）
 2）回退的更好实现方法(解决方案：不需要回退，每一次都多读进一个字符，下次直接使用即可)
 3）一些调用其它函数时候返回不必要的ERROR的解决(例如递归定义的时候出现的后面条件不满足但仍然是正确的情况)（删除这些错误提醒）
 4）if后面的括号问题和表达式的括号的问题，是不是表达式有问题。（原文件错误，无需解决）
 目前预计完成任务时间:2016.4.6
 2016.4.5
 基本完成。
 2016.4.7 再次修改
 2016.4.8 再版
*/

ifstream fin("/Users/mouizumi/Desktop/编译原理实验/Grammer/text.txt ");
string binary;
pair<int,int> judge;

void read(){
    getline(fin,binary);
    stringstream ss(binary);
    int x,y;
    char t1,t2;
    ss>>t1>>x>>t2>>y;
    judge.first = x;
    judge.second = y;
}

bool com = false;
bool program();
bool subprogram();
bool explain();
bool sentences();
bool explaintable();
bool idtable();
bool item();
bool loop();
bool give();
bool complex();
bool boolexpression();
bool relationexpression();
bool relation();
bool sentn();
bool condition();
bool E();
bool I();
bool F();
bool F1();
bool stop = false;

bool program(){
    read();
    //cout<<judge.first<<" "<<judge.second<<endl;
    if(judge.first == 25){
         read();
        if(judge.first == 0){
            read();
            if(judge.first == 17){
                if(subprogram()){
                    return true;
                }else{
                    return false;
                }
            }else{
                cout<<"ERROR 1:";
                cout<<"need a semicolon"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 2:";
            cout<<"need an id"<<endl;
            return false;
        }
    }else{
        cout<<"ERROR 3:";
        cout<<"need a string of PROGRAM"<<endl;
        return false;
    }
}

bool subprogram(){
    if(explain()){
       // read();
       // if(judge.first == 17){
           // read();
            if(judge.first == 28){
                if(sentn()){
                    read();
                    if(judge.first == 29){
                        //return true;
                        read();
                        if(judge.first == 19){
                            return true;
                        }else{
                            cout<<"ERROR 4:";
                            cout<<"NEED A ."<<endl;
                            return false;
                        }
                    }else{
                        cout<<"ERROR 5:";
                        cout<<"need a string of END"<<endl;
                        return false;
                    }
                }else{
                    //cout<<"ERROR 6:";
                    return false;
                }
            }else{
                cout<<"ERROR 7:";
                cout<<"need a string of BEGIN"<<endl;
                return false;
            }
        }
//        else{
//            cout<<"need a semicolon"<<endl;
//            return false;
//        }
//}
    else{
        cout<<"ERROR 8:";
        cout<<2<<endl;
        return false;
    }
}

bool explain(){
    read();
    if(judge.first == 26){
        if(explaintable()){
            //read();
//            if(judge.first == 17){
//                return true;
//            }else{
//                cout<<"need a semicolon"<<endl;
//                return false;
//            }
            return true;
        }else{
            //cout<<"ERROR 9:";
            return false;
        }
    }else{
        cout<<"ERROR 10:";
        cout<<"NEED A STRING OF VAR"<<endl;
        return false;
    }
}

bool explaintable(){
    //read();
    if(idtable()){
       // read();
        if(judge.first == 38){
            read();
            if(judge.first == 36){
                read();
                if(judge.first == 17){
                    //mark = fin.tellg();
                    if(explaintable()){//何时结束？回退？
                        return true;
                    }else{
                       // fin.seekg(mark);   //回退
                        return true ;
                    }
                }else{
                    cout<<"ERROR 11:";
                    cout<<"NEED A SEMICOLON"<<endl;
                    return false;
                }
            }else{
                cout<<"ERROR 12:";
                cout<<"NEED A SORT"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 13:";
            cout<<"NEED A COMMON"<<endl;
            return false;
        }
    }else{
        return false;
    }
}

bool idtable(){
    read();
    if(judge.first == 0){
        read();
        if(judge.first == 18){
            if(idtable()){
                return true;
            }else{
                cout<<"ERROR 15:";
                cout<<"ONE MORE COLON"<<endl;
                return false;
            }
        }else{
            return true;
        }
    }else{
        return false;
    }
}

bool sentences(){
    read();
    if(judge.first == 28){
    if(complex()){
        com = false;
        return true;
    }
    }else if(judge.first == 0){
    if(give()){
        return true;
    }
    }else if(judge.first == 30){
    
    if(condition()){
        return true;
    }
    }else if (judge.first == 33){
    if(loop()){
        return true;
    }
    }
    //cout<<"ERROR 17:";
    return false;
}

bool sentn(){
    if(sentences()){
       // read();
        if(judge.first == 17){
            if(sentn()){
                //read()?
                return true;
            }else{
                cout<<"ERROR 18:";
                cout<<"NEED A SENTENCE"<<endl;
            }
        }else{
           // read();
            return true;
        }
    }
   // cout<<"ERROR 19:";
    return false;
}

bool expression(){
    if(item()){
       // mark = fin.tellg();
        //read();
        while(judge.first == 3){
            if(item()){
                //read();
            }else{
                return true;
            }
        }
    //fin.seekg(mark);
        return true;
    }else{
        cout<<"ERROR 20:";
        cout<<"NEED AN ITEM"<<endl;
        return false;
    }
    return false;
}
bool h(){
    if(boolexpression()){
    return true;
}else{
    cout<<"ERROR 31:";
    cout<<"NEED A BOOLEXPRESSION"<<endl;
    return false;
}
}

bool factor(){
    read();
    while(judge.first == 40){read();}
    if(judge.first == 0 || judge.first == 1){
        return true;
    }
    if(judge.first == 9){
        if(expression()){
            //read();
            if(judge.first == 10){
                return true;
            }else{
                cout<<"ERROR 21:";
                cout<<"NEED A )"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 22:";
            cout<<"NEED AN EXPRESSION"<<endl;
            return false;
        }
    }
    //需要回退

    if(expression()){
        return true;
    }
    cout<<"ERROR 23:";
    cout<<"AN ILLEGAL EXPREESION"<<endl;
    return false;
}


bool item(){
    if(factor()){
        //mark = fin.tellg();
        read();
        while(judge.first == 5){
            if(factor()){
                
                read();
               // continue;
            }else{
                return true;
            }
        }
        return true;
    }else{
        cout<<"ERROR 24:";
        cout<<"NEED A FACTOR"<<endl;
        return false;
    }
    return false;
}

bool boolexpression(){
   if(relationexpression()){
        //read();
        if(judge.first == 24){
            read();
            if(judge.first == 24){
                if(boolexpression()){
                    return true;
                }else{
                    cout<<"ERROR 26:";
                    cout<<"NEED A BOOLEXPRESSION"<<endl;
                    return false;
                }
            }else{
                cout<<"ERROR 27:";
                cout<<"NEED A &"<<endl;
                return false;
            }
        }else if(judge.first == 23){
            read();
            if(judge.first == 23){
                if(boolexpression()){
                    return true;
                }else{
                    cout<<"ERROR 28:";
                    cout<<"NEED A BOOLEXPRESSION"<<endl;
                    return false;
                }
            }else{
                cout<<"ERROR 29:";
                cout<<"NEED A | "<<endl;
                return false;
            }
        }else{
            return true;
        }
//        }else{
//            cout<<"ERROR 30:";
//            cout<<"NEED A && OR ||"<<endl;
//            return false;
//        }
}
    read();

    return false;
}

bool relationexpression(){
    stop = false;
    read();
    if(judge.first==9 || judge.first==0 || judge.first == 1){
        stop = true;
    if(F()){
        if(relation()){
            stop = false;
            if(F()){
                return true;
            }else{
                cout<<"ERROR 32:";
                cout<<"NEED AN EXPRESSION"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 33:";
            cout<<"NEED AN RELATION"<<endl;
            return false;
        }
    }
    }
    if(judge.first == 40){
        return boolexpression();
    }else{
        cout<<"ERROR 34:";
        cout<<"NEED AN EXPRESSION"<<endl;
        return false;
    }
}

bool relation(){
   // read();
    if(judge.first == 7||judge.first == 8 || judge.first == 9 || judge.first == 17 || judge.first == 13 || judge.first == 14 || judge.first == 15){
        return true;
    }
    //cout<<"ERROR 35:";
    return false;
}

bool loop(){
    //read();
    if(judge.first == 33){
        if(boolexpression()){
            //read();
            if(judge.first == 34){
                if(sentences()){
                    return true;
                }else{
                    cout<<"ERROR 36:";
                    cout<<"NEED AN SENTENCES"<<endl;
                    return false;
                }
            }else{
                cout<<"ERROR 37:";
                cout<<"LESS OF DO"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 38:";
            cout<<"NEED A BOOLEXPRESSION"<<endl;
            return false;
        }
    }else{
        cout<<"ERROR 39:";
        cout<<"NEED A WHILE"<<endl;
        return false;
    }
}

bool give(){
   // read();
    if(judge.first == 0){
        read();
        if(judge.first ==12){
            //read();
            stop = false;
            if(F()){
                return true;
            }else{
                cout<<"ERROR 40:";
                cout<<"NEED AN EXPRESSION"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 41:";
            cout<<"NEED A :="<<endl;
            return false;
        }
    }else{
        cout<<"ERROR 42:";
        cout<<"NEED AN ID"<<endl;
        return false;
    }
}

bool complex(){
    
   // read();
    com = true;
    if(judge.first == 28){
        if(sentn()){
            //read();
            if(judge.first == 29){
                read();
                return true;
            }else{
                cout<<"ERROR 43:";
                cout<<"NEED AN END"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 44:";
            return false;
        }
    }else{
        cout<<"ERROR 45:";
        cout<<"NEED A BEGIN"<<endl;
        return false;
    }
    return false;
}

bool condition(){
   // read();
    if(judge.first == 30){
        if(boolexpression()){
            //read();
            if(judge.first == 31){
                if(sentences()){
                    if(judge.first == 29 && com) {return true;}
                    //read();
                    //if(judge.first == 30) return condition();
                    if(judge.first == 32){
                        if(sentences()){
                            return true;
                        }else{
                            cout<<"ERROR 48:";
                            cout<<"NEED A SENTENCE"<<endl;
                        }
                    }else{
                        return true;
                    }
                }else{
                    cout<<"ERROR 46:";
                    return false;
                }
            }else{
               cout<<"ERROR 49";
                cout<<"NEED THEN"<<endl;
            }
        }else{
            cout<<"ERROR 50:";
            cout<<"NEED A BOOLEXPRESSION"<<endl;
        }
    }else{
        cout<<"ERROR 51:";
        cout<<"NEED AN IF"<<endl;
    }
   // cout<<"ERROR 47:";
    return false;
}


bool E(){
    if(I()){
        //read();
        if(judge.first == 3){
            if(I()){
                //read();
                return true;
            }
        }else{
            return true;
        }
    }
    return false;
}

bool I(){
    if(F()){
        //read();
        if(judge.first == 5){
            if(F()){
                //read();
                return true;
            }
        }else{
            return true;
        }
    }
    return false;
}

bool F(){
    if(!stop)read();
    stop = false;
    if(judge.first == 9){
        if(E()){
            stop = false;
            if(judge.first == 10){
                if(!stop) read();
                stop = false;
                if(F1()){
                    return true;
                }
            }else{
                cout<<"ERROR 52:NEED A )"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR 53: NEED AN EXPRESSION"<<endl;
            return false;
        }
    }
    if(judge.first == 1){
        if(!stop) read();
        stop = false;
        if(judge.first!=5 && judge.first !=3) {stop=true;return true;}
        if(F1()){
            return true;
        }else{
            cout<<"ERROR 54:NEED AN EXPRESSION "<<endl;
            return false;
        }
    }
    if(judge.first == 0){
        if(!stop) read();
        stop = false;
        if(judge.first!=5 && judge.first !=3) {stop=true;return true;}
        if(F1()){
            return true;
        }else{
            cout<<"ERROR:NEED AN EXPREESION"<<endl;
            return false;
        }
    }
    return false;
}

bool F1(){
    //read();
    if(judge.first == 5){
        if(F()){
            if(!stop) read();
            stop = false;
            if(judge.first!=5 && judge.first !=3) {stop=true;return true;}
            if(F1()){
                return true;
            }else{
                cout<<"ERROR:NEED AN EXPREESION"<<endl;
                return false;
            }
        }else{
            cout<<"ERROR:NEED AN EXPREESION"<<endl;
            return false;
        }
    }
    if(judge.first == 3){
        if(F()){
            
            if(!stop) read();
            stop = false;
            if(judge.first!=5 && judge.first !=3) {stop=true;return true;}
            if(F1()){
                return true;
            }else{
                cout<<"ERROR:NEED AN EXPREESION"<<endl;
            }
        }else{
            cout<<"ERROR:NEED AN EXPREESION"<<endl;
            return false;
        }
    }
    return true;
}



int main(){
    if(program()){
        cout<<"True"<<endl;
    }else{
        cout<<"False"<<endl;
    }
    return 0;
}



/*
 #define ID 0;
 #define NUM 1;
 #define KEY 25;
 #define PLUS 3;
 #define MINUS 4;
 #define TIMES 5;
 #define SUB 6;
 #define GT  7;
 #define ST  8;
 #define LK  9;
 #define RK  10;
 #define NO 11;
 #define EQUAL 12;
 #define SE 13;
 #define LE 14;
 #define NE 15;
 #define EQ 16
 #define FH 17;
 #define DH 18;
 #define JH 19;
 #define KZ 20;
 #define ZS 21;
 table["program"] = 25;
 table["var"] = 26;
 table["procedure"] = 27;
 table["begin"] = 28;
 table["end"] = 29;
 table["if"] = 30;
 table["then"] = 31;
 table["else"] = 32;
 table["while"] = 33;
 table["do"] = 34;
 table["call"] = 35;
 table["integer"] = 36;
 table["real"] = 37;
 
 
c 1.<程序> → program id ; <程序体>
c 2.<程序体> → <变量说明> begin <语句串> end .      去掉了分号
c 3. <变量说明> → var <变量说明表>;
c 4. <变量说明表> → <变量表>：<类型> | <变量表>：<类型>；<变量说明表>    <类型>后有分号?
c 5. <类型> → integer
c 6. <变量表> → <变量> | <变量>,<变量表>        分号改逗号？
c 7.<语句串> → <语句> | <语句>;<语句串>
c 8. <语句> → <复合语句>|<赋值语句>|<条件语句>|<循环语句>
c 9.< 复合语句> → begin <语句串>end
c 10.<赋值语句> → id:=<表达式>
c 11.<条件语句> → if<布尔表达式>　then　<语句>
 ｜if<布尔表达式>　then　<语句> 　else <语句>
d 12.<循环语句> → while　<布尔表达式>　do　<语句>
dc 13. <表达式> → <项>｜<项>+<项>
c 14.<项> → <因子>｜<因子>*<因子>
dc 15. <因子> → <表达式>　| (<表达式>) | <标识符> | <常数>
dc 16.<布尔表达式> → <关系表达式> | ！<布尔表达式>
 | <布尔表达式> && <布尔表达式>
 | <布尔表达式> ||　<布尔表达式>
c 17.< 关系表达式> → <表达式><关系><表达式>
c 18. <关系> → <　|　<=　|　>　|　>=　|　=　|　<>
 
13 14 15的左递归消除：
E-表达式  I-项  F-因式 C-标识符 N-数字
E->I|I+I 
I->F|F*F
F->(E)F'|NF'|CF'
F'->*FF'|+FF'|*F+F*FF'|ε   ==>F'-> *FF'|+FF'|ε
 */
