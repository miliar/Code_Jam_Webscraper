#include<iostream>
#include<string>
#include<fstream>

using namespace std;

bool ya(const string&lista){
	for (int i = 0; i < lista.length(); i++){
		if (lista[i] == '-')return false;
	}
	return true;
}

void mostrar(string&tort){
	for (int ctrl = 0; ctrl < tort.length(); ctrl++){
		cout << tort[ctrl];
	}
	cout << '\n';
}

void darlavuelta(string&tortita, int&cont){
	string mem = tortita.substr(0, cont+1);
	for (int i = 0; i < mem.length(); i++){
		if (mem[i] == '+')mem[i] = '-';
		else mem[i] = '+';
	}
	for (int ctrl = 0; ctrl < mem.length(); ctrl++){
		tortita[ctrl] = mem[mem.length() - ctrl - 1];
	}
}

void resolvercaso(string&tortita, int&fin){
	int mem = tortita.length() - 1;
	for (mem; tortita[mem] == '+'; mem--){
	}
	if(tortita[0]=='-')darlavuelta(tortita, mem);
	else{
		int ctrl;
		for (ctrl = 0; tortita[ctrl] != '-'; ctrl++){
			tortita[ctrl] = '-';
		}
	}
	fin = mem;
}

int main(){
	string tortitas;
	int casos;
	int cont;
	ifstream ent;
	ofstream sal;
	sal.open("salida.txt");
	ent.open("entrada.txt");

	ent >> casos;
	int num;
	int ini;
	num = 1;
	for (int ctrl = 0; ctrl < casos; ctrl++){
		cont = 0;
		ent >> tortitas;
		int res = tortitas.length() - 1;
		ini = 0;
		while (!ya(tortitas)){
			resolvercaso(tortitas, res);
			cont++;
		}
		sal << "Case #" << num << ": ";
		sal << cont << '\n';
		num++;
	}
}