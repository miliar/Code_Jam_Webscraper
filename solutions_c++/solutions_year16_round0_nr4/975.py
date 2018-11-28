// Problema_code_jam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <time.h>
#include <limits.h>
//ULLONG_MAX
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <windows.h>
#include <fstream>
#include "math.h"
#include <vector>
#include <string>
#include <iomanip>
using namespace std;
typedef unsigned long long int ll;
typedef signed long long int sll;
double PI = 3.141592653589793;
//Problema
ifstream in("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\D-large.in", ios_base::in);
ofstream out("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\D-large_out.in", ios_base::out);

void pre_process()
{
	return;
}
void case_solve()
{
	ll K, C, S;
	in >> K >> C >> S;
	//Verificar se é impossível
	if (S*C < K)
	{
		out << "IMPOSSIBLE";
		return;
	}
	//Verificar se a complexidade é um	
	ll i;
	if (C == 1)
	{
		for (i = 1; i <= K; i++)
		{
			out << i;
			if (i != K) out << " ";
		}
		return;
	}
	
	
	//Posicionar estudantes
	vector<vector<ll>> stud;
	ll students = 1;
	while (!(students*C >= K)) students++;
	//construtir
	vector<ll> aux;
	for (i = 1; i <= C; i++) aux.push_back(1);
	for (i = 1; i <= students; i++) stud.push_back(aux);
	//preeencher
	ll j;
	ll prox = 1;
	for (i = 0; i <= students - 1; i++)
	{
		for (j = 0; j <= C - 1; j++)
		{
			if(prox <=K) stud[i][j] = prox;
			prox++;
		}
	}
	//Calcular as posições
	vector<ll> pos;
	for (i = 0; i <= stud.size() - 1; i++)
	{
		ll linha = 2;
		ll soma = K*(stud[i][0]-1)+(stud[i][1]-1);
		if (C > 2)
		{
			while (true)
			{
				//Calcula a soma dessa linha
				soma = soma*K + (stud[i][linha] - 1);
				//fim?
				if (linha == C - 1) break;
				linha++;
			}
		}
		soma++;
		pos.push_back(soma);
	}
	//Imprimi a resposta
	for (i = 0; i <= pos.size() - 1; i++)
	{
		out << pos[i];
		if (i != pos.size() - 1) out << " ";
	}
		




	//in >> L >> X;
	//getline(in, linha);
	//out << fixed << setprecision(6);   escreve  0.123456
	//cout << setfill('0') << setw(5) << 25;    output: 00025
	//out << "YES";


}
int _tmain(int argc, _TCHAR* argv[])
{

	ll i, cases;
	pre_process();
	in >> cases;
	for (i = 1; i <= cases; i++)
	{
		if (i == 2)
		{
			i = i;
		}
		out << "Case #" << i << ": ";
		case_solve();
		cout << "Caso " << i << " de " << cases << " --> OK\n";
		out << "\n";
	}
}