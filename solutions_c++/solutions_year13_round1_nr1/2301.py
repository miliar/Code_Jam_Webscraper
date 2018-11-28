// GCJ.cpp : Defines the entry point for the console application.
//
#include "stdio.h"
#include "stdafx.h"
#define _USE_MATH_DEFINES
#include "math.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int numTestes;
	int quantidadeTinta;
	int tamanhoCirculoInicial;
	int circulosPintados;
	scanf("%d", &numTestes);
	for(int i = 1; i <= numTestes; i++){
		scanf("%d %d", &tamanhoCirculoInicial, &quantidadeTinta);
		circulosPintados = 0;
		double tintaSobrando = quantidadeTinta;
		tamanhoCirculoInicial++;
		while(tintaSobrando >= 0){
			tintaSobrando = tintaSobrando - ((tamanhoCirculoInicial * tamanhoCirculoInicial) - ((tamanhoCirculoInicial - 1) * (tamanhoCirculoInicial - 1)));
			tamanhoCirculoInicial += 2;
			if(tintaSobrando >= 0){
				circulosPintados++;
			}
		}
		printf("Case #%d: %d\n", i, circulosPintados);
	}
	return 0;
}

