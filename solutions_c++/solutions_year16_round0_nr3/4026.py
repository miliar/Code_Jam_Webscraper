CC=g++
FLAGS=-std=c++11
EXE = q3

prog: q3.o
	$(CC) $(FLAGS) -o $(EXE) q3.o
	
q3.o: q3.cpp
	$(CC) $(FLAGS) -c q3.cpp
	
run: prog
	@./$(EXE)
	
clean:
	@rm *.o $(EXE)