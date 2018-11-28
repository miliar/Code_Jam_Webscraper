CC=g++
FLAGS=-std=c++11
EXE = q1

prog: q1.o
	$(CC) $(FLAGS) -o $(EXE) q1.o
	
q1.o: q1.cpp
	$(CC) $(FLAGS) -c q1.cpp
	
run: prog
	@./$(EXE)
	
clean:
	@rm *.o $(EXE)