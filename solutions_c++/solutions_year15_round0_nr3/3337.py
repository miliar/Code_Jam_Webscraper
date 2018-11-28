#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
struct quat{
	char symb;
	int sign;
	quat(){
		symb=0;
		sign=0;
	}
	quat(char sy){
		symb=sy;
		}
	quat(int si){
		sign=si;
	}
	quat(char sy,int si=1){
		symb=sy;
		if (!si)sign=-1;
		else sign=si;
	}
};
quat product(quat f, quat s);
bool Find(string full, quat end, quat fin, int sti, int chk);
quat tabl[4][4];
int main()
{
	ifstream ifile;
	ofstream ofile;
	ifile.open("input.in");
	ofile.open("output.txt");
	tabl[0][0] = quat('1',1);tabl[0][1] = quat('i',1);tabl[0][2] = quat('j',1);tabl[0][3] = quat('k',1);
	tabl[1][0] = quat('i',1);tabl[1][1] = quat('1', 0);tabl[1][2] = quat('k',1);tabl[1][3] = quat('j', 0);
	tabl[2][0] = quat('j',1);tabl[2][1] = quat('k', 0);tabl[2][2] = quat('1',0);tabl[2][3] = quat('i',1);
	tabl[3][0] = quat('k',1);tabl[3][1] = quat('j',1);tabl[3][2] = quat('i',0);tabl[3][3] = quat('1', 0);
	
	int t,len1,len2,x,gotCom;
	string rep,full;
	ifile>>t;
	for (int a=1; a<=t; a++)
	{
		full="";
		x=1;
		gotCom=0;
		ifile>>len1>>len2;
		ifile>>rep;
		for(int z=1;z<=len2;z++)
			full=full+rep;
		quat fin(full[0],1);
		gotCom=Find(full,quat('i',1), fin,1,0);
		if (gotCom)
			ofile<<"Case #"<<a<<": YES"<<endl;
		else 
			ofile<<"Case #"<<a<<": NO"<<endl;
	}
	return 0;
}

quat product(quat f, quat s){
	int row, col;
	if (f.symb == '1')
		row =0;
	else if(f.symb == 'i')
		row =1;
	else if(f.symb == 'j')
		row =2;
	else if(f.symb == 'k')
		row =3;
	if (s.symb == '1')
		col =0;
	else if (s.symb == 'i')
		col =1;
	else if (s.symb == 'j')
		col =2;
	else if (s.symb == 'k')
		col =3;
	quat pro =tabl[row][col];
	pro.sign =(f.sign*s.sign*pro.sign);
	return pro;
}
bool Find(string full, quat end, quat fin, int sti, int chk){
	for (int a=sti; a<=full.length();a++){
		if (fin.sign ==end.sign && fin.symb == end.symb){
			if (chk==0){
				return (Find(full, quat('j',1), quat(full[a],1), a+1, 1));
			}
			else if (chk==1){
				return (Find(full, quat('k',1), quat(full[a],1), a+1, 2));
			}
			else if (full.length()==a)
				return true;
		}
		if(a>=full.length())break;
		quat tem(full[a],1);
		fin=product(fin, tem);
	}
	return false;
}