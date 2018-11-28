t = gets.to_i
result = Array.new(t)
t.times do |i|
  File.open("large-#{i}.in", 'w') do |f|
    f.puts 1
    n = gets.to_i
    f.puts n
    n.times do
      f.puts gets
    end
  end
end
